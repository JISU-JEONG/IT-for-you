from django.db import models

# Create your models here.
class ProblemBasic(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_category = models.CharField(max_length=200)
    p_question = models.TextField()
    p_type = models.IntegerField()
    p_diff = models.IntegerField()
    p_code = models.TextField(null=True)
    class Meta:
        managed = False
        db_table = 'problems'

class AnswerBasic(models.Model):
    a_id = models.AutoField(primary_key=True)
    p_id = models.ForeignKey(ProblemBasic, db_column='p_id', on_delete=models.CASCADE)
    a_value = models.TextField()
    a_correct = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'answers'