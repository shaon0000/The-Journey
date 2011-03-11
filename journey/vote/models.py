from django.db import models


class UserVote(models):
	CHOICES = (('USEFUL', 'useful',), ('FUNNY','funny',), ('COOL','cool',), ('BLING','bling'),)
	SCORE_CHOICES = ((x, x,) for x in range(1, 6))
	user = models.ForeignKey(User)
	project = models.ForeignKey(Project)
	vote_type = models.CharField(max_length=32, choices=CHOICES)
	score = IntegerField(choices=SCORE_CHOICES)

class Project(models):
	name = models.CharField(max_length=1024, required=True)
	description = models.TextField()

    def stat(self):
        """Return a dictionary of score types and the corresponding average"""
        votes = UserVote.objects.filter(project=self)
        stat_dict = {}
        
        # the self.CHOICES dictionary contains two parts, where only the first index is needed
        for choice, verbose in UserVote.CHOICES:
            vote_type_list = votes.filter(vote_type=choice)
            avg_score = sum(x.score for x in vote_type_list)/len(vote_type_list)
            stat_dict[choice] = avg_score
        
        return stat_dict


class ProjectMember(models):
	user = models.ForeignKey(User)
	project = models.ForeignKey(Project)
    def __unicode__(self):
        return '%s %s' % (user.first_name, user.last_name)


