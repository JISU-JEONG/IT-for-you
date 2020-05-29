from django.db import models
from accounts.models import User
from problems.models import Problem
# Create your models here.

class Interview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    prob = models.ForeignKey(Problem, on_delete=models.CASCADE)    
    content = models.CharField(max_length=500)
    file = models.FileField(upload_to='interviews/')
