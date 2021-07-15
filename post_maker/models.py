from django.db import models
from UserApp.models import User
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 50)
    body = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)
    date_modified = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title + " " + self.author





