# Generated by Django 3.0.6 on 2020-06-06 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_article_menuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='postid',
            field=models.CharField(default='', max_length=120),
        ),
    ]
