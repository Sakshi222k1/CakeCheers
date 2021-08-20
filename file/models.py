from django.db import models

class upload_file(models.Model):
    Timestamp=models.CharField(max_length=15,blank=True)
    Username=models.CharField(max_length=50,blank=True)
    Cleanliness=models.TextField(max_length=50,blank=True)
    Water_Supply=models.TextField(max_length=50,blank=True)
    Light_Condition=models.CharField(max_length=10,blank=True)
    Smell=models.CharField(max_length=10,blank=True)
    Comment=models.TextField(max_length=50,blank=True)



    def __str__(self):
        return self.Comment
