# Generated by Django 2.0.2 on 2018-11-12 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20181112_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletags',
            name='name',
            field=models.CharField(max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='articletype',
            name='name',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
