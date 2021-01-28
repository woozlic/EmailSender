from django.forms import ModelForm, TextInput, EmailInput, DateInput, NumberInput, FileInput
from .models import SendDocs
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

class SendDocsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SendDocsForm, self).__init__(*args, **kwargs)
        self.fields['docs'].required = True

    class Meta:
        model = SendDocs
        fields = ['name', 'date_birth', 'salary', 'email', 'docs']
        widgets = {
            'name': TextInput(attrs={}),
            'date_birth': DateInput(attrs={'type': 'date'}),
            'salary': NumberInput(attrs={}),
            'email': EmailInput(attrs={}),
            'docs': FileInput(attrs={}),
        }

    def __str__(self):
        return self.name

    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            SendDocs.objects.get(name=name)
            raise ValidationError("Такое имя уже есть в базе данных")
        except SendDocs.DoesNotExist:
            pass
        return name

    def clean_salary(self):
        salary = self.cleaned_data['salary']
        if salary <= 0:
            raise ValidationError("Зарплата должна быть больше 0!")
        return salary

class EditDocsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditDocsForm, self).__init__(*args, **kwargs)
        self.fields['docs'].required = True

    class Meta:
        model = SendDocs
        fields = ['name', 'date_birth', 'salary', 'email', 'docs']
        widgets = {
            'name': TextInput(attrs={}),
            'date_birth': DateInput(attrs={'type': 'date'}),
            'salary': NumberInput(attrs={}),
            'email': EmailInput(attrs={}),
            'docs': FileInput(attrs={}),
        }

    def __str__(self):
        return self.name

    def clean_salary(self):
        salary = self.cleaned_data['salary']
        if salary <= 0:
            raise ValidationError("Зарплата должна быть больше 0!")
        return salary
