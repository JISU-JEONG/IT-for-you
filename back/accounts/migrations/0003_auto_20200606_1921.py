# Generated by Django 3.0.6 on 2020-06-06 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprob',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
