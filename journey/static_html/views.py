from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def mobile(request):
    params = {}
    params['user'] = request.user
    return render_to_response('mobile.html', params)

@login_required
def ballot(request):
    params = {}
    params['user'] = request.user
    return render_to_response('ballot.html', params)
