# Generated by Django 2.2.6 on 2020-04-07 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20200407_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
