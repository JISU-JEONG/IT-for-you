import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from problems.models import Problem
# Create your models here.
class User(AbstractUser):
    pass
    # incorrects = models.ManyToManyField(
    #     Problem,
    #     related_name='incorrect',
    #     blank=True,
    #     through='Xnote'
    # )
    
# class Xnote(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)    
#     prob = models.ForeignKey(Problem, on_delete=models.CASCADE)    
#     u_answer = models.CharField(max_length=500)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class UserProb(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prob = models.ForeignKey(Problem, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    