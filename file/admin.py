from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path
from django.shortcuts import render
from .models import upload_file
from django import forms
from .models import upload_file
import csv , io
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from django.core.mail import send_mail

#from django_mail_admin import mail
# Register your models here.
from .models import upload_file

class CsvImportForm(forms. Form):
    csv_upload =forms.FileField()

class upload_fileAdmin(admin.ModelAdmin):
    list_display=('Timestamp','Username','Cleanliness','Water_Supply','Light_Condition','Smell','Comment')
    def get_urls(self):
        urls= super().get_urls()
        new_urls=[path('upload-csv/', self.upload_csv),]
        return new_urls +urls


    def upload_csv(self,request):

        print("OUT POST")
        if request.method =="POST":

            csv_file= request.FILES.get('csv_file')
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)

            with open('csvfile.pickle', 'wb') as f:
                pickle.dump(csv_file, f)

            with open('csvfile.pickle', 'rb') as f:
                d = pickle.load(f, encoding='latin1')

                df=pd.read_csv(d)
                comment=[]
                for i in df['Comment']:
                    comment.append(i)

                df=df.drop(["Timestamp","Username","Comment"],axis=1)

                df['Smell']=df['Smell'].replace("Neutral",2.5)
                df['Smell']=df['Smell'].replace("Good",5)
                df['Smell']=df['Smell'].replace("Bad",2.5)

                def meancal(col):
                    sum=0
                    count=0
                    for i in col:
                        sum=sum+int(i)
                        count=count+1
                    h_mean=sum/count
                    return h_mean

                overall=[]
                clean=meancal(df['Cleanliness'])
                overall.append(clean/5)
                water=meancal(df['Water_Supply'])
                overall.append(water/5)
                light=meancal(df['Light_Condition'])
                overall.append(light/5)
                smell=meancal(df['Smell'])
                overall.append(smell/5)
                print('\r\n')
                print("-----------------*------------------")
                print('\r\n')
                print("Average condition of Cleanliness",clean)
                print("Average condition of Water Supply",water)
                print("Average condition of Light Condition",light)
                print("Average condition of Smell",smell)
                print('\r\n')
                print("-----------------*------------------")
                print('\r\n')

                sum=0
                count=0
                for i in overall:
                    sum=sum+i
                    count=count+1
                overall_avg=round(((sum/count)*5),1)
                print("Overall Rating of the washroom on the scale of 1-5:",overall_avg)
                print('\r\n')
                print("-----------------*------------------")
                print('\r\n')
                print("Comments of the people are:")
                for i in comment:
                    print(i)
                print('\r\n')
                print("-----------------*------------------")
                print('\r\n')

                hyg=round(clean,1)
                wat=round(water,1)
                toi=round(light,1)
                odo=round(smell,1)
                subject = 'WASHROOM A: FEEDBACK ANALYSIS'
                message = 'FEEDBACK ANALYSIS:\n\n Overall Cleanliness Rating: {0}\n Overall Water Supply Rating: {1}\n Overall Light Condition Rating: {2}\n Overall Smell Rating: {3}\n\n Overall Rating of the washroom on the scale of 1-5:{4}\n\n Comments of the people are: {5}\n'.format(hyg, wat,toi,odo,overall_avg,comment)

                send_mail(
                subject,
                message,
                'feedbackmonitoring123@gmail.com',
                ['sakshibansal2k1@gmail.com','mangalsezal11900@gmail.com','444pankhurimahajan@gmail.com','prachigarg58977@gmail.com'],#,'garimapant05@gmail.com'],
                #context = Context({'user': "Hi"},
                fail_silently=False,
                )






            file_data=csv_file.read().decode("utf-8")

            io_string = io.StringIO(file_data)
            next(io_string)
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):

                _,created=upload_file.objects.update_or_create(
                    Timestamp=column[0],
                    Username=column[1],
                    Cleanliness=column[2],
                    Water_Supply=column[3],
                    Light_Condition=column[4],
                    Smell=column[5],
                    Comment=column[6]

                )


            form=CsvImportForm()
            data= {"form": form}
            return render(request, "../template/admin/csv_upload.html",data)
        # return HttpResponse("HELLO")
        return render(request, "../template/admin/csv_upload.html",)




admin.site.register(upload_file, upload_fileAdmin)
