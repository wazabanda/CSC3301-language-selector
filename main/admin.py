from django.contrib import admin
from .models import *
# Register your models here.

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name','paradigms','group','taken']
    list_editable = ['taken']

admin.site.register(Group)
admin.site.register(Language,LanguageAdmin)
