# Generated by Django 2.1.1 on 2019-02-08 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20190207_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created',
            field=models.DateField(auto_now=True),
        ),
    ]
