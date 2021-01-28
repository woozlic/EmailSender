from django.db import models

# Create your models here.

class SendDocs(models.Model):

    name = models.CharField(max_length=50, verbose_name="Имя", unique=True)
    date_birth = models.DateField(verbose_name="Дата рождения")
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    email = models.EmailField(max_length=50)
    docs = models.FileField(upload_to="documents/%Y/%m/%d")

    def __str__(self):
        return self.name
