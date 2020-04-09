from django.db import models
from django.contrib.auth.models import User

class Blogs(models.Model):
    title    = models.CharField(max_length=200, default='heading goes here')
    description = models.TextField(max_length=5000, default='')
    time = models.DateTimeField(auto_now_add= True )
    picture = models.ImageField(upload_to='blogpictures')

    def __str__(self):
        return self.title


class Profile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE, default = '')
    description = models.TextField(max_length=500, default = "i am very good person")
    profilepic = models.ImageField(upload_to='profilepictures' , default = 'images/profile.png' )


    def __str__(self):
        return f'{self.user.username} profile'
