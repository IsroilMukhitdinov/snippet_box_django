from django.shortcuts import redirect, render

# Create your views here.

def snippet(request):
    return render(request, 'snippet/snippet.html', {'title' : 'Snippet'})

    # if request.user.is_authenticated():
    # else:
    #     return redirect('login-page')
