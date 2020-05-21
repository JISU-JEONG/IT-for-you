from django.contrib import admin
from .models import *
# Register your models here.
class ProbCateAdmin(admin.ModelAdmin):
    list_display = ('pc_id', 'pc_value',)
    ordering = ('pc_id',)
admin.site.register(ProbCate, ProbCateAdmin)

class ProbTypeAdmin(admin.ModelAdmin):
    list_display = ('pt_id', 'pt_value',)
admin.site.register(ProbType, ProbTypeAdmin)

class ProbDiffAdmin(admin.ModelAdmin):
    list_display = ('pd_id', 'pd_value',)
admin.site.register(ProbDiff, ProbDiffAdmin)

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('p_id', 'p_question', 'pc_id', 'pt_id', 'pd_id',)
    # ordering = ('p_id',)
admin.site.register(Problem, ProblemAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('a_id', 'p_id', 'a_value', 'a_correct',)
    # ordering = ('p_id',)
admin.site.register(Answer, AnswerAdmin)