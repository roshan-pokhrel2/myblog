from django.shortcuts import render , redirect
from . forms import userRegistrationForm, blogform, profileform
from django.http import  HttpResponse
from django.contrib import messages
from .models import Blogs, Profile
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import  User
from django.core.paginator import Paginator

def home(request):
    contex = {'title': 'home'}
    return render(request, 'home.html', contex)


def register(request):
    if request.method == 'POST':
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, 'your account has been created as ' + username)
    else:
        form = userRegistrationForm()
    contex = {'form': form, 'title': 'register'}
    return render(request, 'register.html', contex)

@login_required()
def blogpost(request):
    if request.method == 'POST':
        form = blogform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your blog has succesfully uplaoded')
    else:
        form = blogform()
    contex = {'form': form, 'title': 'blogpost'}
    return render(request, 'addblog.html', contex)


def blog(request):
    blog = Blogs.objects.all().order_by('-time')
    obj  = Paginator(blog, 5)
    page_number = request.GET.get('page')
    page_obj = obj.get_page(page_number)
    contex = {'blog': blog,  'obj':page_obj}
    return render(request, 'blog.html', contex)


def logging(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, 'you have successfully login into your account')
        else:
            
            messages.error(request, 'user name and password didnot match. try again ')
    
    return redirect('home')

@login_required()
def loggingout(request):
    logout(request)
    messages.success(request, 'you have successfully logout your account ')
    return redirect('home')


def details(request, pk):
    blogpost = Blogs.objects.filter(pk=pk).values()
    contex = {'title':'fullpost', 'blogpost':blogpost}
    return render(request , 'fullpost.html', contex)

@login_required()
def profilefun(request):
    if request.method == 'POST':
        form = profileform(request.POST, request.FILES , instance= request.user)
        if form.is_valid():
            form.save()
    else:
        form = profileform()
    contex = {'title':'profile' , 'form':form}
    return render(request , 'profile.html' , contex)



