# Generated by Django 2.2.6 on 2020-04-09 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0016_auto_20200409_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilepic',
            field=models.ImageField(default='images/profile.png', upload_to='profilepictures'),
        ),
    ]
