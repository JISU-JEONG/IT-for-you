from django.db import models
from accounts.models import User
from problems.models import Problem
# Create your models here.

class MyProb(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  prob = models.ForeignKey(Problem, on_delete=models.CASCADE)