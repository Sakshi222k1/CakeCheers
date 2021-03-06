# Generated by Django 3.2.3 on 2021-08-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_auto_20210804_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload_file',
            name='feedback',
        ),
        migrations.RemoveField(
            model_name='upload_file',
            name='questions',
        ),
        migrations.AddField(
            model_name='upload_file',
            name='Comment',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='upload_file',
            name='Hygiene',
            field=models.TextField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='upload_file',
            name='Odour',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='upload_file',
            name='Timestamp',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='upload_file',
            name='Toilet_seat',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='upload_file',
            name='Water_supply',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
