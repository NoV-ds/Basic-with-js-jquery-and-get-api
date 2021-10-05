from django.shortcuts import redirect, render, HttpResponse
from .models import UserProfile, usercommunity
from django.core.mail import send_mail
from Basic.settings import EMAIL_HOST_USER
from django.contrib.auth import authenticate
import json
# Create your views here.

def index(request):
    return render(request, 'index.html')

def Signup(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']
        user = UserProfile(fullname=fullname, email=email, password=password)
        user.save()
        if user:
            username = email
            password = password
            mail(username, password)
        return redirect('login')
    else:
        return render(request, 'signup.html')

def mail(username, password):
    receiver = username
    subject = 'Your Registration is Successfull'
    message = 'Welcom to MySite \nYour registration is successfull \nYour Username: {}\nYour Password: {}\n\nThanks!'.format(username, password)
    return send_mail(subject, message, EMAIL_HOST_USER, [receiver], fail_silently=False)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = (username, password)
        authenticate(user)
        return redirect('index')
    else:
        return render(request, 'login.html')

def get_data(request, name):
    if request.method == 'GET':
        query = UserProfile.objects.get(fullname = name)
        query1 = usercommunity.objects.get(fullname=query.pk)
        response = json.dumps({'name':query.fullname, 'email':query.email, 'community':query1.community})
        return HttpResponse(response, content_type='text/json')