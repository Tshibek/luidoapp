# Generated by Django 3.2.5 on 2021-08-26 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210810_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monterdaily',
            name='daily_montage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daily_montage', to='core.dailymontage'),
        ),
    ]
