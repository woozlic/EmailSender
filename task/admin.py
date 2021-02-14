from django.contrib import admin
from .models import SendDocs, License, ReportHistory

# Register your models here.

admin.site.register(SendDocs)
admin.site.register(License)
admin.site.register(ReportHistory)
