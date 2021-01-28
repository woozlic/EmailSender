# Generated by Django 3.1.5 on 2021-01-27 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senddocs',
            name='docs',
            field=models.FileField(upload_to='documents/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='senddocs',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Имя'),
        ),
    ]
