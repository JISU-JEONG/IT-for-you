from django.db import models
# Create your models here.
class ProbCate(models.Model):
    pc_id = models.AutoField(primary_key=True)
    pc_value = models.CharField(max_length=200)
    class Meta:
        managed = False
        db_table = 'prob_cate'

    # def __str__(self):
    #     return self.pc_value

class ProbType(models.Model):
    pt_id = models.AutoField(primary_key=True)
    pt_value = models.CharField(max_length=200)
    class Meta:
        managed = False
        db_table = 'prob_type'

class ProbDiff(models.Model):
    pd_id = models.AutoField(primary_key=True)
    pd_value = models.CharField(max_length=200)
    class Meta:
        managed = False
        db_table = 'prob_diff'

class Problem(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_question = models.TextField()
    p_code = models.TextField(null=True)
    pc_id = models.ForeignKey(ProbCate, db_column='pc_id', on_delete=models.CASCADE)
    pt_id = models.ForeignKey(ProbType, db_column='pt_id', on_delete=models.CASCADE)
    pd_id = models.ForeignKey(ProbDiff, db_column='pd_id', on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'problems'

class Answer(models.Model):
    a_id = models.AutoField(primary_key=True)
    p_id = models.ForeignKey(Problem, db_column='p_id', on_delete=models.CASCADE)
    a_value = models.TextField()
    a_correct = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'answers'
