from vote.models import UserVote, Project, ProjectMember
from django.contrib import admin

admin.site.register(UserVote)
admin.site.register(Project)
admin.site.register(ProjectMember)
