from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['user']
        first_name = request.POST['Fname']
        last_name = request.POST['Lname']
        email = request.POST['email']
        password = request.POST['pass']
        confirm_password = request.POST['cpass']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User is already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                                first_name=first_name,
                                                last_name=last_name,
                                                email=email,
                                                password=password
                                                )
                user.save()
                print("User is created")
                messages.info(request, 'Registration Successful')
                return redirect('/')

        else:
            print("User not created")
            messages.info(request, "Password not matched")
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print("login success")
            return redirect('/')

        else:
            messages.info(request, 'Invalid user')
            print("login error")
            return redirect('login')

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return  redirect('login')

