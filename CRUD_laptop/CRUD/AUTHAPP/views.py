from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from random import randint
# Create your views here.

otp = randint(1000,9999)

def registerView(request):
    form = UserCreationForm()
    template_name = 'AUTHAPP/register.html'
    context = {'form': form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST.get('username')

            subject = "Signup alert"
            message = 'you have sign up in with your email'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email,]
            send_mail(subject, message, email_from, recipient_list)


            return redirect('login_url')

    return render(request, template_name, context)

def loginView(request):
    template_name = 'AUTHAPP/login.html'
    context = {}
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')


        user = authenticate(username=un, password=pw)
        if user is not None:
            login(request, user)
            subject = "login alert"
            message = f'otp is {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.username,]
            send_mail(subject,message,email_from,recipient_list)

            return redirect('verify')

        else:
            messages.error(request, template_name, context)

    return render(request, template_name, context)


def logoutView(request):
    logout(request)
    return redirect('login_url')

def twostepView(request):
    template_name = 'AUTHAPP/twostep.html'
    context = {}

    if request.method == 'POST':
        otp1 = request.POST.get('otp')
        otp2 = int(otp1)

        if otp2 == otp:
            return redirect('laptopform_url')
        else:
            messages.error(request, "Invalid OTP")

    return render(request, template_name, context)