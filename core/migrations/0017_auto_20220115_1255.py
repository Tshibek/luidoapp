# Generated by Django 3.2.5 on 2022-01-15 11:55

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_montagevideogallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='montagevideogallery',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='montagevideogallery',
            name='height',
        ),
        migrations.RemoveField(
            model_name='montagevideogallery',
            name='width',
        ),
        migrations.AlterField(
            model_name='montagevideogallery',
            name='file',
            field=models.FileField(upload_to=core.models.montage_video_path),
        ),
    ]
