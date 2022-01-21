from django.shortcuts import render

from snippet.models import Snippet

# Create your views here.

context = {
    'snippets' : Snippet.objects.all(),
    'title' : 'Home'
}

def home(request):
    return render(request, 'home/home.html', context)
