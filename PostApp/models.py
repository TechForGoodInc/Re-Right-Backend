from django.db import models
from UserApp.models import User
from django.utils import timezone
import datetime


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    # date_created = models.DateTimeField(default = timezone.now)
    # image = models.ImageField()
    # date_modified = models.DateTimeField(auto_now = True)
    # author = models.ForeignKey(User, on_delete = models.CASCADE)
    # no_of_likes = models.IntegerField()
    # no_of_comments = models.IntegerField()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.today)

    class Meta:
        ordering = ["-date"]

        # unique_together means same user can not like the same post more than once.
        unique_together = (('user', 'post'),)
        index_together = (('user', 'post'),)
