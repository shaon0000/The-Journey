"""
This is the page we use to authenticate whether a 
user is a Yelp user.It will probably involve sending 
the username/password to some third party site and 
getting a boolean back. 

For testing purposes, we will use django authenticated
users. In production, the django auth will get replaced.

Steps to replace authentication:

a) locate AUTHENTICATION_BACKENDS in settings.py
 - django runs through that list to authenticate a user
 - if all of them fails, user is not authenticated
b) journey.yelp_auth.py will be added to that list

c) The following code will be uncommented and built:


class YelpAuth:
    def authenticate(self, username, password):
        # check the username/password and return a User
        authentic = check(username, password) # <--- THIS IS WHERE WE ASK YELP TO CHECK CRED FOR US
        if authentic:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User.objects.create(username=username, password='does not matter')
            return user
        else:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
"""
