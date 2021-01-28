# Generated by Django 3.1.5 on 2021-01-27 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SendDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('date_birth', models.DateField(verbose_name='Дата раождения')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('email', models.EmailField(max_length=50)),
                ('docs', models.FileField(upload_to='')),
            ],
        ),
    ]