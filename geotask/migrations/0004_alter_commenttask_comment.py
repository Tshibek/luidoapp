# Generated by Django 3.2.5 on 2021-12-03 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geotask', '0003_task_monters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commenttask',
            name='comment',
            field=models.TextField(),
        ),
    ]
