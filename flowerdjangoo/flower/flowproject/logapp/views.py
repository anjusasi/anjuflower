from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from . models import Flower


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('book')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        con_password = request.POST['con_password']
        if password == con_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name)
                user.save()
                messages.success(request, 'You have Successfully registered')
                return redirect('login')
        else:
            messages.info(request, 'password not matched')
            return redirect('register')
        return redirect('/')

    return render(request, 'registration.html')

def book(request):
    if request.method == 'POST':
        customername = request.POST['customername']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        address = request.POST['address']
        quantity = request.POST['quantity']
        city = request.POST['slct2']
        item = request.POST['item']
        district = request.POST['slct1']
        fl = Flower(customername=customername,phonenumber=phonenumber,email=email,address=address,
                    quantity=quantity,city=city,item=item,district=district)
        fl.save()
        messages.success(request, 'your order has successfully placed')

    return render(request, 'booking.html')

def logout(request):
    auth.logout(request)
    return redirect('/')