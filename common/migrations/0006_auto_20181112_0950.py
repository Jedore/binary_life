# Generated by Django 2.0.2 on 2018-11-12 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20181109_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='articles', to='common.TagsType'),
        ),
    ]
