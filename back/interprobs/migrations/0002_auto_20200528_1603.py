# Generated by Django 3.0.6 on 2020-05-28 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interprobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='file',
            field=models.FileField(upload_to='interviews/'),
        ),
    ]
