# Generated by Django 3.2.5 on 2021-12-05 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20211202_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailymontage',
            name='date',
            field=models.DateField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='monter',
            name='name',
            field=models.CharField(db_index=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='monterdaily',
            name='date',
            field=models.DateField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='monterdaily',
            name='status',
            field=models.CharField(blank=True, choices=[('PRACUJE', 'PRACUJE'), ('L4', 'L4'), ('URLOP', 'URLOP'), ('UŻ', 'UŻ'), ('NB', 'NB')], db_index=True, default='PRACUJE', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team',
            field=models.CharField(db_index=True, max_length=15, unique=True),
        ),
    ]