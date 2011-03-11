from django.db import models

class Yelper(models.Model):
    """Defines a general Yelp user who can vote."""
    username = models.CharField(max_length=100, blank=False)

    def my_votes(self):
        """Return a list of companies and what the user voted them."""
        vote_query = YelperVote.objects.filter(user=self)
        info = []
        projects = Project.objects.all()

        for project in projects:
            data = {}
            data['name'] = project.name
            data['description'] = project.description
            data['members'] = list(x.user.username for x in ProjectMember.objects.filter(project=project))
            data['stats'] = {}
            
            for choice, verbose in YelperVote.CHOICES:
                try:
                    vote = vote_query.get(project=project, vote_type=choice).score
                except YelperVote.DoesNotExist:
                    vote = 0 
                data['stats'][choice] = vote

            info.append(data)
        return info

class Project(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField()

    def stat(self):
        """Return a dictionary of score types and the corresponding average"""
        votes = YelperVote.objects.filter(project=self)
        stat_dict = {}
        
        # the self.CHOICES dictionary contains two parts, where only the first index is needed
        for choice, verbose in YelperVote.CHOICES:
            vote_type_list = votes.filter(vote_type=choice)
            avg_score = sum(x.score for x in vote_type_list)/len(vote_type_list)
            stat_dict[choice] = avg_score
        
        return stat_dict

class YelperVote(models.Model):
    CHOICES = (('USEFUL', 'useful'), ('FUNNY','funny'), ('COOL','cool'), ('BLING','bling'),)
    SCORE_CHOICES = tuple((x, x) for x in range(0, 6))
    user = models.ForeignKey(Yelper)
    project = models.ForeignKey(Project)
    vote_type = models.CharField(max_length=32, choices=CHOICES)
    score = models.IntegerField(choices=SCORE_CHOICES)
    
    def __unicode__(self):
        return 'user: %s,\nproject: %s,\ntype : %s,\nscore: %s\n' % (self.user.username, self.project.name, self.vote_type, self.score) 
    class Meta:
        unique_together = ('vote_type', 'project', 'user')

class ProjectMember(models.Model):
    user = models.ForeignKey(Yelper)
    project = models.ForeignKey(Project)
    def __unicode__(self):
        return '%s %s' % (user.first_name, user.last_name)

