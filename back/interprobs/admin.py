from django.contrib import admin
from .models import *
# Register your models here.
class InterviewAdmin(admin.ModelAdmin):
    interview = '__all__'
    # ordering = ('p_id',)
admin.site.register(Interview, InterviewAdmin)