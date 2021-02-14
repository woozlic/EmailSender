from django.db import models

# Create your models here.


class SendDocs(models.Model):

    email = models.EmailField(max_length=50)
    docs = models.FileField(upload_to="documents/%Y/%m/%d")

    def __str__(self):
        return self.docs.name


class License(models.Model):

    home_address = models.CharField(max_length=250, verbose_name='Адрес многоквартирного дома')
    company = models.CharField(max_length=250, verbose_name='Наименование/ ФИО лицензиата')
    date_start = models.DateField(verbose_name='Дата начала полномочий по управлению домом', null=True)
    date_end = models.DateField(verbose_name='Дата окончания полномочий по управлению домом', null=True)
    reason_to_exclude = models.CharField(max_length=250, verbose_name='Основание исключения', null=True)
    inn = models.CharField(max_length=50, verbose_name='ИНН')
    date_changed = models.DateField(verbose_name='Дата последнего изменения', null=True)

    def __str__(self):
        return self.home_address


class ReportHistory(models.Model):

    event = models.CharField(max_length=30, verbose_name='Событие')
    home_address = models.CharField(max_length=250, verbose_name='Адрес многоквартирного дома')

    prev_company = models.CharField(max_length=250, verbose_name='Наименование/ ФИО лицензиата')
    prev_inn = models.CharField(max_length=50, verbose_name='ИНН')
    prev_date_start = models.DateField(verbose_name='Дата начала полномочий по управлению домом', null=True)
    prev_date_end = models.DateField(verbose_name='Дата окончания полномочий по управлению домом', null=True)
    prev_reason_to_exclude = models.CharField(max_length=250, verbose_name='Основание исключения', null=True)

    new_company = models.CharField(max_length=250, verbose_name='Наименование/ ФИО лицензиата')
    new_inn = models.CharField(max_length=50, verbose_name='ИНН')
    new_date_start = models.DateField(verbose_name='Дата начала полномочий по управлению домом', null=True)

    date_changed = models.DateField(verbose_name='Дата произошедшего события', null=True)

    def __str__(self):
        return f'{self.event} - {self.home_address}'
