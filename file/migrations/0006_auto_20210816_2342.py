# Generated by Django 3.2.3 on 2021-08-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0005_alter_upload_file_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload_file',
            old_name='Hygiene',
            new_name='Cleanliness',
        ),
        migrations.RenameField(
            model_name='upload_file',
            old_name='Odour',
            new_name='Light_Condition',
        ),
        migrations.RenameField(
            model_name='upload_file',
            old_name='Toilet_seat',
            new_name='Smell',
        ),
        migrations.RenameField(
            model_name='upload_file',
            old_name='Water_supply',
            new_name='Water_Supply',
        ),
        migrations.AddField(
            model_name='upload_file',
            name='Username',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
