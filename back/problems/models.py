from django.db import models

# Create your models here.
class MultipleChoice(models.Model):
    category = models.CharField(max_length=10)
    question = models.TextField()
    