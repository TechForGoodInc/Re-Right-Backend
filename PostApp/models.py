from django.db import models
from UserApp.models import User
from django.utils import timezone
# Create your models here.

class Tag(models.Model):
    label = models.CharField(max_length=20)

    def __str__(self):
        return self.label

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    # date_created = models.DateTimeField(default = timezone.now)
    # image = models.ImageField()
    # date_modified = models.DateTimeField(auto_now = True)
    # author = models.ForeignKey(User, on_delete = models.CASCADE)
    # no_of_likes = models.IntegerField()
    # no_of_comments = models.IntegerField()
    #date_created = models.DateTimeField(default = timezone.now)
    #image = models.ImageField()
    #date_modified = models.DateTimeField(auto_now = True)
    #author = models.ForeignKey(User, on_delete = models.CASCADE)
    #no_of_likes = models.IntegerField()
    #no_of_comments = models.IntegerField()
    #Reports can have multiple tags, tags could be assigned to multiple reports
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.title

    def getTitle(self):
        title = input("please enter the title of your post")
        self.title = title

    def getBody(self):
        body = input("please enter the body for your post")
        self.body = body

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.today)


    class Meta:
        ordering = ["-date"]











