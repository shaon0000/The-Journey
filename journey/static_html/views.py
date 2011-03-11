from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def mobile(request):
    return render_to_response('mobile.html')

def ballot(request):
    return render_to_response('ballot.html')
