# Create your views here.
from journey.vote.models import Project, ProjectMember, UserVote
from django.utils.simplejson.encoder import JSONEncoder as json_encode
from django.utils.simplejson.decoder import JSONDecoder as json_decode
from django.http import HttpResponse
from django.shortcuts import render_to_response

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

         
    
