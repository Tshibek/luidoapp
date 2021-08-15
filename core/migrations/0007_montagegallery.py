# Generated by Django 3.2.5 on 2021-08-04 04:36

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_montagepaid_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='MontageGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to=core.models.montage_gallery_path)),
                ('date', models.DateField(auto_now_add=True)),
                ('montage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.montagepaid')),
            ],
        ),
    ]