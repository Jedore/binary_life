# Generated by Django 2.0.2 on 2018-11-13 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_articlecomments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomments',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='common.ArticleComments'),
        ),
    ]
