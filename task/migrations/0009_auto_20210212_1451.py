# Generated by Django 3.1.5 on 2021-02-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_reporthistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporthistory',
            name='date_changed',
            field=models.DateField(null=True, verbose_name='Дата произошедшего события'),
        ),
        migrations.AlterField(
            model_name='license',
            name='date_changed',
            field=models.DateField(null=True, verbose_name='Дата последнего изменения'),
        ),
    ]
