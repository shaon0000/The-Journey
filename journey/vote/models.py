from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	name = models.CharField(max_length=1024, blank=False)
	description = models.TextField()

class ProjectMember(models.Model):
	user = models.ForeignKey(User)
	project = models.ForeignKey(Project)

class UserVote(models.Model):
	CHOICES = (('USEFUL', 'useful',), ('FUNNY','funny',), ('COOL','cool',), ('BLING','bling'),)
	SCORE_CHOICES = ((x, x,) for x in range(1, 6))
	user = models.ForeignKey(User)
	project = models.ForeignKey(Project)
	vote_type = models.CharField(max_length=32, choices=CHOICES)
	score = models.IntegerField(choices=SCORE_CHOICES)

class User(models.Model):
	username = models.CharField(max_length=100, blank=False)

