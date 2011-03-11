# Create your views here.
from journey.vote.models import Project, ProjectMember, UserVote
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import json

@login_required
def get_all(request):
    """Get a JSON string containing all projects, members of projects, and project votes"""
    info = []
    projects = Project.objects.all()
    
    for project in projects:
        data_dict = {}
        data_dict['name'] = project.name
        data_dict['members'] = ProjectMember.objects.filter(project=project)
        data_dict['stats'] = project.stat()
        info.append(data_dict)
    return HttpResponse(json.dumps(info), mimetype='application/json')

@login_required
def get_my_votes(request):
    """Get a JSON string containing all projects that a user voted on"""
    user = request.user
    info = UserVote.objects.my_votes(user)
    return HttpResponse(json.dumps(info), mimetype='application/json')

@login_required
def project(request):
    """POST/GET system to deal with retrieving/adding projects"""
    if request.POST:
        name = request.POST.get('name', None)
        description = request.POST.get('description','')
        Project.objects.create(name=name, description=description)
        return HttpResponse('1')
    else:
        id = request.GET['id']
        project = Project.objects.get(id=id)
        return HttpResponse(json.dumps(project.get_dict()), mimetype='application/json')

@login_required
def add_myself_to_team(request):
    """Add yourself to a team"""
    if request.POST:
        id = request.POST.get('id', None)
        if not id:
            return HttpResponseBadRequest('no id of project given')
        try:
            project = Project.objects.get(id=id)
        except Project.DoesNotExist:
            return HttpResponseBadRequest('does not exist, bad ID')
        project_member = ProjectMember.object.create(user=request.user, project=project)
        return HttpResponse('1')
    else:
        return HttpResponseBadRequest('must be a POST command')

@login_required
def vote(request):
    if request.POST:
        # post a change of a vote
        user = request.user
        project_id = request.POST['project_id']
        vote_type = request.POST['vote_type']
        score = request.POST['score']
        project = Project.objects.get(id=project_id)
        
        obj, _ = UserVote.objects.get_or_create(user=user, project=project, vote_type=vote_type)
        obj.score = score
        obj.save()
        return HttpResponse('1')
    elif request.GET:
        # get the current score for a vote
        user = request.user
        project_id = request.GET.get('project_id', None)
        vote_type = request.GET.get('vote_type', None)
        if not (project_id and vote_type):
            return HttpResponseBadRequest('project id or vote type was not given')

        project = Project.objects.get(id=project_id)
        
        obj, _ = UserVote.objects.get_or_create(user=user, project=project, vote_type=vote_type)
        return HttpResponse(obj.score)
 
