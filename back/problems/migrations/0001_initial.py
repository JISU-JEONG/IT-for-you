# Generated by Django 3.0.6 on 2020-05-26 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('a_id', models.AutoField(primary_key=True, serialize=False)),
                ('a_value', models.TextField()),
                ('a_correct', models.BooleanField()),
            ],
            options={
                'db_table': 'answers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProbCate',
            fields=[
                ('pc_id', models.AutoField(primary_key=True, serialize=False)),
                ('pc_value', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'prob_cate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProbDiff',
            fields=[
                ('pd_id', models.AutoField(primary_key=True, serialize=False)),
                ('pd_value', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'prob_diff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_question', models.TextField()),
                ('p_code', models.TextField(null=True)),
            ],
            options={
                'db_table': 'problems',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProbType',
            fields=[
                ('pt_id', models.AutoField(primary_key=True, serialize=False)),
                ('pt_value', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'prob_type',
                'managed': False,
            },
        ),
    ]
