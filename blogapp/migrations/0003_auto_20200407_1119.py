# Generated by Django 2.2.6 on 2020-04-07 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_remove_blogs_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='total_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogapp.blogs'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
