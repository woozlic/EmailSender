from django.shortcuts import render, redirect
from .forms import SendDocsForm
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import SendDocs
from .make_report import upload_xlsx, make_xlsx, update_report_history, str_to_date
from datetime import date, datetime, timedelta
from django.core.exceptions import ValidationError
import os

from django.conf import settings

# Create your views here.


def index(request):
    sent = False
    if request.method == 'POST':
        form = SendDocsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            cd = form.cleaned_data

            file = cd['docs']

            try:
                file_date = file.name.split(' ')[6]
            except IndexError:
                raise ValidationError('Название файла должно быть вида "Реестр лицензий субъекта РФ 74 на 05.02.2021 04-19-24.xlsx"')

            # report = upload_xlsx(file, file_date)
            today = [str_to_date(file_date)]
            week = [str_to_date(file_date), str_to_date(file_date)+timedelta(7)]
            # update_report_history(report)
            today_report = make_xlsx(today)
            week_report = make_xlsx(week)

            subject = f"Отчет за такое число."
            message = f"Отчет за такое число."
            email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [cd['email']])
            # email.attach(today_report, today_report.read(), today_report.content_type)
            # email.attach(week_report, week_report.read(), week_report.content_type)
            email.attach_file(today_report)
            email.attach_file(week_report)

            try:
                result = email.send()
                messages.success(request, f"Вы добавили информацию в БД и отправили письмо на {cd['email']}")
            except:
                messages.error(request, f"Что-то пошло не так, не удалось отправить письмо.")
        else:
            print(form.errors)
    else:
        form = SendDocsForm()
    return render(request, 'task/index.html', {'form': form, 'sent': sent})


def all(request):
    path = settings.MEDIA_ROOT + '\\reports'
    all_objects = os.listdir(path)
    return render(request, 'task/all.html', {'all_objects': all_objects})


# def edit(request, id):
#     try:
#         obj = SendDocs.objects.get(id=id)
#         current_file = obj.docs
#         if request.method == 'POST':
#             form = EditDocsForm(instance=obj, data=request.POST, files=request.FILES)
#             if form.is_valid():
#                 cd = form.cleaned_data
#                 obj.name = cd['name']
#                 obj.email = cd['email']
#                 obj.salary = cd['salary']
#                 obj.date_birth = cd['date_birth']
#                 obj.docs = cd['docs']
#                 obj.save()
#                 msg = 'Вы успешно изменили объект'
#                 current_file = obj.docs
#                 messages.success(request, msg)
#             else:
#                 messages.error(request, 'Ошибка при изменении данных')
#         else:
#             form = EditDocsForm(instance=obj)
#         return render(request, 'task/edit.html', {'form': form, 'current_file': current_file})
#     except SendDocs.DoesNotExist:
#         return redirect('all')


def delete_post(request, id):
    try:
        obj = SendDocs.objects.get(id=id)
        obj.delete()
        return redirect('all')
    except SendDocs.DoesNotExist:
        return redirect('all')
