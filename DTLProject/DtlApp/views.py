from django.shortcuts import render, redirect
from django.http import HttpResponse
from DtlApp.forms import UserReg, Updateuser, UpdateProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from DtlApp.models import Update
from Sample import settings
from django.core.mail import send_mail
# Create your views here.


def demo(request):
    return HttpResponse('From DTL APP')


def home(request):
    return render(request, 'DtlApp/home.html')


def about(request):
    return render(request, 'DtlApp/about.html')


def contact(request):
    return render(request, 'DtlApp/contact.html')


def register(request):
    if request.method == "POST":
        data = UserReg(request.POST)
        if data.is_valid():
            data.save()
            username = data.cleaned_data.get('username')
            messages.success(
                request, "hii {} you are successfully registered".format(username))
            return redirect("/dtl/login")
    else:
        data = UserReg()
        return render(request, 'DtlApp/register.html', {'data': data})


@login_required
def dashboard(request):
    return render(request, 'DtlApp/dashboard.html')


@login_required
def profile(request):
    return render(request, 'DtlApp/profile.html')


@login_required
def update(request):
    if request.method == "POST":
        c = Updateuser(request.POST, instance=request.user)
        y = UpdateProfile(request.POST, request.FILES,
                          instance=request.user.update)
        if c.is_valid() and y.is_valid():
            c.save()
            y.save()
            messages.success(
                request, "{} your details updated successfully".format(request.user.username))
            return redirect("/dtl/profile")
    c = Updateuser(instance=request.user)
    y = UpdateProfile(instance=request.user.update)
    return render(request, 'DtlApp/update.html', {'c': c, 'y': y})


@login_required
def mailsend(request):
    p = User.objects.values_list("email", flat=True)
    # print(P)
    if request.method == "POST":
        # rec = request.POST['receiver'].split(",")
        z = []
        a = request.user.email
        rs = list(filter(None, p))
        for n in rs:
            if n == " " or n == a:
                continue
            else:
                z.append(n)
        print(z)
        sub = request.POST['subject']
        msg = request.POST['message']
        snd = settings.EMAIL_HOST_USER
        t = send_mail(sub, msg, snd, z)
        if t == 1:
            messages.success(
                request, "Mail send to {} Successfully".format(z))
            return redirect('/dtl/mailsend')
        messages.warning(
            request, "Mail doesn't send due to invalid mail id {}".format(z))
    return render(request, 'DtlApp/mailsend.html')
