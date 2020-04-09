# Generated by Django 2.2.6 on 2020-04-07 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
