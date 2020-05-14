from django.db import models

# Create your models here.
class ProblemBasic(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_category = models.CharField(max_length=200)
    p_question = models.TextField()
    p_type = models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'problems'