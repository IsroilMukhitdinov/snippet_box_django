from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def login(request):
    if request.method == 'POST':
        client_username = request.POST['username']
        client_password = request.POST['password']
        # client = User.objects.filter(username = client_username, password = client_password).first()
        # if client is not None:
        #     return redirect('home-page')
        # else:
        #     return redirect('login-page')
        client =  authenticate(username = client_username, password = client_password)
        if client is not None:
            return redirect('home-page')



    return render(request, 'login/login.html')