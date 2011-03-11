# Create your views here.
from journey.vote.models import Project, ProjectMember, YelperVote, Yelper
from django.utils.simplejson.encoder import JSONEncoder as json_encode
from django.utils.simplejson.decoder import JSONDecoder as json_decode
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
    return HttpResponse(json_encode(info), mimetype='application/json')

@login_required
def get_my_votes(request):
    """Get a JSON string containing all projects that a user voted on"""
    user = request.user
    info = UserVote.objects.my_votes(user)
    return HttpResponse(json_encode(info), mimetype='application/json')

@login_required
def vote(request):
    if request.POST:
        # post a change of a vote
        user = request.user
        project_id = request.POST['project_id']
        vote_type = request.POST['vote_type']
        score = request.POST['score']
        project = Project.objects.get(id=project_id)
        
        obj, _ = YelperVote.objects.get_or_create(user=user, project=project, vote_type=vote_type)
        obj.score = score
        obj.save()
        return HttpResponse('1')
    elif request.GET:
        # get the current score for a vote
        user = request.user
        project_id = request.GET['project_id']
        vote_type = request.GET['vote_type']
        project = Project.objects.get(id=project_id)
        
        obj, _ = YelperVote.objects.get_or_create(user=user, project=project, vote_type=vote_type)
        return HttpResponse(obj.score)

@login_requred
def get_vote(request):
    user = request.user
    project_id = request.POST['project_id']
    vote_type = request.POST['vote_type']
    score = request.POST['score']
    project = Project.objects.get(id=project_id)
    try:
        obj = YelperVote.objects.get(user=user, project=project, vote_type=vote_type)
    except YelperVote.DoesNotExist:
        
