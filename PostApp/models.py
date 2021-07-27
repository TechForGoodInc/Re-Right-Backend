from django.db import models
from UserApp.models import User
from django.utils import timezone
# Create your models here.
import datetime

class Post(models.Model):

    class Tag(models.TextChoices):
        ARTICLE1 = 'BF', _('We are all Born Free')
        ARTICLE2 = 'DD', _("Don't Discriminate")
        ARTICLE3 = 'RL', _('Right to Life')
        ARTICLE4 = 'NS', _('No Slavery')
        ARTICLE5 = 'NT', _('No Torture')
        ARTICLE6 = 'WG', _('Rights No Matter Where You Go')
        ARTICLE7 = 'AE', _('All Equal Before the Law')
        ARTICLE8 = 'PL', _('Human Rights are Protected by Law')
        ARTICLE9 = 'UD', _('No Unfair Detainment')
        ARTICLE10 = 'RT', _('Right to Trial')
        ARTICLE11 = 'IG', _('Innocent Till Proven Guilty')
        ARTICLE12 = 'RP', _('Right to Privacy')
        ARTICLE13 = 'FM', _('Freedom to Move')
        ARTICLE14 = 'SP', _('Right to Seek a Safe Place to Live')
        ARTICLE15 = 'RN', _('Right to a Nationality')
        ARTICLE16 = 'MF', _('Marriage and Family')
        ARTICLE17 = 'OT', _('Right to Your Own Things')
        ARTICLE18 = 'FT', _('Freedom of Thought')
        ARTICLE19 = 'FE', _('Freedom of Expression')
        ARTICLE20 = 'PA', _('Right to Public Assembly')
        ARTICLE21 = 'RD', _('Right to Democracy')
        ARTICLE22 = 'SS', _('Social Security')
        ARTICLE23 = 'WR', _("Worker's Rights")
        ARTICLE24 = 'RTP', _('Right to Play')
        ARTICLE25 = 'FS', _('Food and Shelter for All')
        ARTICLE26 = 'RE', _('Right to Education')
        ARTICLE27 = 'CR', _('Copyright')
        ARTICLE28 = 'FF', _('Fair and Free World')
        ARTICLE29 = 'RB', _('Responsibility')
        ARTICLE30 = 'TA', _('No One Can Take Away Your Human Rights')


    title = models.CharField(max_length=50)
    body = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)
    image = models.ImageField()
    date_modified = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    no_of_likes = models.IntegerField()
    no_of_comments = models.IntegerField()
    #Reports can have multiple tags, tags could be assigned to multiple reports
    tags = models.CharField(max_length=3, choices=Tag.choices)
    objects = models.Manager()
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

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('time',)

    def getBody(self):
        body = input("please enter the body of your comment")
        self.body = body









