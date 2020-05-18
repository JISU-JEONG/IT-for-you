from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    user = ('id', 'username')
    # ordering = ('p_id',)
admin.site.register(User, UserAdmin)