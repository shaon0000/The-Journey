from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response

def user_login(request):
    if request.POST:
        # login form was submitted
        next = request.POST.get('next', '/booth/')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return render_to_response('login.html', {'error': 'Your account has been disabled'})
        else:
            return render_to_resposne('login.html', {'error': 'incorrect password/username combination'})
    else:
        # login form was requested
        next = request.GET.get('next','/booth/')
        return render_to_response('login.html',{'next':next})

@login_required
def logout_user(request):
  logout(request)
  return HttpResponseRedirect('/login/')



