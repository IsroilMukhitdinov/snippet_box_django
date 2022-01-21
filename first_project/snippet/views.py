from django.shortcuts import redirect, render

# Create your views here.

def snippet(request):
    if request.user.is_authenticated():
        return render(request, 'snippet/snippet.html', {'title' : 'Snippet'})
    else:
        return redirect('login-page')
