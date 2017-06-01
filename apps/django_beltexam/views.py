from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.db.models import Count
# Create your views here.
def index(request):
    context = {
    "user" : User.objects.all()
    }
    print User.objects.all()
    return render(request, 'django_beltexam/index.html', context)

def register(request):
    postData = {
        'username': request.POST['username'],
        'email': request.POST['email'],
        'password': request.POST['password'],
        'confirm': request.POST['confirm'],
    }
    user_array = User.objects.register(postData)
    # print user_array
    # print postData
    errors = User.objects.register(postData)
    if len(errors) == 0:
        request.session['id'] = User.objects.get(email=postData['email'])[0].id
        request.session['username'] = postData['username']
        return redirect('/secrets')
    else:
        for error in errors:
            messages.info(request, error)
            return redirect('/')

def login(request):
    postData = {
        'email': request.POST['email'],
        'password': request.POST['password'],
    }
    # print postData
    errors = User.objects.login(postData)
    if len(errors) == 0:
        request.session['id'] = User.objects.get(email=postData['email'])[0].id
        request.session['username'] = User.objects.get(username=postData['username'])
        return redirect('/pokes')
    else:
        for error in errors:
            messages.info(request, error)
    return redirect('/')

def count_poke(request):
	redirect('/pokes')

def showboard(request):
	redirect('/pokes')

def logout(request):
	request.session.pop('id')
	return redirect('/')












