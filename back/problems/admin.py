from django.contrib import admin
from .models import *
# Register your models here.
class MultipleChoiceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category', 'question')
    ordering = ('pk',)
admin.site.register(MultipleChoice, MultipleChoiceAdmin)