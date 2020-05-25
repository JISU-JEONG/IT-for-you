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
    uncorrets = models.ManyToManyField(
        Problem,
        related_name='uncorret',
        blank=True
    )

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)