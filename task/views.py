from django.shortcuts import render, redirect
from .forms import SendDocsForm, EditDocsForm
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import SendDocs

from django.conf import settings

# Create your views here.

def index(request):
    sent = False
    if request.method == 'POST':
        form = SendDocsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            cd = form.cleaned_data
            subject = f"Здравствуйте, {cd['name']}. Ваш адрес был внесен в тестовую таблицу."
            message = f"Имя - {cd['name']}, дата рождения - {cd['date_birth']}, зарплата - {cd['salary']}."
            email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [cd['email']])

            file = cd['docs']
            email.attach(file.name, file.read(), file.content_type)

            try:
                result = email.send()
                form.save()
                messages.success(request, f"Вы добавили информацию в БД и отправили письмо на {cd['email']}")
            except:
                messages.error(request, f"Что-то пошло не так, не удалось отправить письмо.")
    else:
        form = SendDocsForm()
    return render(request, 'task/index.html', {'form': form, 'sent': sent})

def all(request):
    all_objects = SendDocs.objects.all()
    return render(request, 'task/all.html', {'all_objects': all_objects})

def edit(request, id):
    try:
        obj = SendDocs.objects.get(id=id)
        current_file = obj.docs
        if request.method == 'POST':
            form = EditDocsForm(instance=obj, data=request.POST, files=request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                obj.name = cd['name']
                obj.email = cd['email']
                obj.salary = cd['salary']
                obj.date_birth = cd['date_birth']
                obj.docs = cd['docs']
                obj.save()
                msg = 'Вы успешно изменили объект'
                current_file = obj.docs
                messages.success(request, msg)
            else:
                messages.error(request, 'Ошибка при изменении данных')
        else:
            form = EditDocsForm(instance=obj)
        return render(request, 'task/edit.html', {'form': form, 'current_file': current_file})
    except SendDocs.DoesNotExist:
        return redirect('all')

def delete_post(request, id):
    try:
        obj = SendDocs.objects.get(id=id)
        obj.delete()
        return redirect('all')
    except SendDocs.DoesNotExist:
        return redirect('all')
