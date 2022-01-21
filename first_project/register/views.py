from unicodedata import name
from django.shortcuts import redirect, render



# Create your views here.

def register(request):
    if request.method == 'POST':
        client_username = request.POST['username']
        client_password = request.POST['password']
        client_email = request.POST['email']
        print(client_username, client_password, client_email)
        return redirect('home-page')
   
    return render(request, 'register/register.html', {'title' : 'Register'})




















# from .forms import RegistrationForm 
# form = RegistrationForm()
# context = {'form' : form}