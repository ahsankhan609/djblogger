# to generate fake data for the test
import factory
from django.contrib.auth.models import User

from blog.models import *

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = 'testuser'
    password = 'testpassword'
    is_superuser = True
    is_staff = True
    
class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
        
    title ='x'
    subtitle ='x'
    slug = 'x'
    author = factory.SubFactory(UserFactory)
    content = 'x'
    status = 'published'