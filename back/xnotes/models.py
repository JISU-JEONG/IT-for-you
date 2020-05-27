from django.db import models
from accounts.models import User
from problems.models import Problem
# Create your models here.
class Xnote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    prob = models.ForeignKey(Problem, on_delete=models.CASCADE)    
    u_answer = models.CharField(max_length=500)