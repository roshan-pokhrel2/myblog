# Generated by Django 2.2.6 on 2020-04-07 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20200407_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='total_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogapp.blogs'),
        ),
    ]
