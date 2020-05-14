from django.contrib import admin
from .models import *
# Register your models here.
class ProblemBasicAdmin(admin.ModelAdmin):
    list_display = ('p_id', 'p_category', 'p_question', 'p_type')
    # ordering = ('p_id',)
admin.site.register(ProblemBasic, ProblemBasicAdmin)