# Generated by Django 4.1.3 on 2022-12-26 06:32

import django.core.validators
from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_myvideos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myvideos',
            name='video',
            field=models.FileField(upload_to=home.models.UploadToPathAndRenameVideo('media/video/'), validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'wmv', 'flv', 'avi', 'avchd ', 'webm', 'ogg'])]),
        ),
    ]
