# Generated by Django 4.1.3 on 2022-12-26 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_folder_created_date_myvideos_video_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='myvideos',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]