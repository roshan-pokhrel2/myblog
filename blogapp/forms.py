from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Blogs, Profile

class userRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class blogform(forms.ModelForm):
    class Meta:
        model = Blogs
       
        fields = '__all__'

class profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('description', 'profilepic')
       
        
