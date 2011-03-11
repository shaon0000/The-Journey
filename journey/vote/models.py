from django.db import models
from django.contrib.auth.models import User

class Project(models):
	name = models.CharField(max_length=1024, required=True)
	description = models.TextField()

class ProjectMember(models):
	user = models.ForeignKey(User)
	project = models.ForeignKey(Project)

class UserVote(models):
	CHOICES = (('USEFUL', 'useful',), ('FUNNY','funny',), ('COOL','cool',), ('BLING','bling'),)
	SCORE_CHOICES = ((x, x,) for x in range(1, 6))
	user = models.ForeignKey(User)
	project = models.ForeignKey(Project)
	vote_type = models.CharField(max_length=32, choices=CHOICES)
	score = IntegerField(choices=SCORE_CHOICES)

class User(models):
	username = models.CharField(max_length=100, required=True)

