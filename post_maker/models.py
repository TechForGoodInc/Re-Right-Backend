from django.db import models
from UserApp.models import User
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 50)
    body = models.TextField()
    #date_created = models.DateTimeField(default = timezone.now)
    #image = models.ImageField()
    #date_modified = models.DateTimeField(auto_now = True)
    #author = models.ForeignKey(User, on_delete = models.CASCADE)
    #no_of_likes = models.IntegerField()
    #no_of_comments = models.IntegerField()

    def __str__(self):
        return self.title










