"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from journey.vote.models import Project, UserVote, ProjectMember, User

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

class UserTest(TestCase):
    def setUp(self):
        """Create a general set of objects that User class uses frequently"""
        self.user = User.objects.create(username='test_user')
        self.project = Project.objects.create(name='test_project', description='This is a test!')
        self.project_member = ProjectMember.objects.create(user=self.user, project=self.project)
        for choice, verbose in UserVote.CHOICES:
            UserVote.objects.create(user=self.user, project=self.project, vote_type=choice, score=3)
        print 'it worked!' 
    def test_my_votes(self):
        """
        Given one project, one user, and a few set of votes all set to three, 
        check if my_votes returns correct results
        """
        data = UserVote.objects.my_votes(self.user)
        try:
            assert data == [{'name': 'test_project', 'description':'This is a test!', 'members': ['test_user'], 'stats': dict((x, 3) for x, y in UserVote.CHOICES)}]
        except AssertionError:
            import pdb
            pdb.set_trace()
__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> 1 + 1 == 2
True
"""}

