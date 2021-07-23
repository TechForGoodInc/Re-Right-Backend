from django.db.models.deletion import CASCADE, PROTECT
from UserApp.models import User
from django.db import models

#Is table necessary for Tags?
class Tag(models.Model):
    label = models.CharField(max_length=20)

    def __str__(self):
        return self.label

class Report(models.Model):
    title = models.CharField(max_length=255)
    suspect_description = models.TextField()
    report_description = models.TextField()
    location = models.CharField(max_length=255)

    #if we're sending reports to a human rights org, status changes
    REPORT_STATUS_PENDING = 'P'
    REPORT_STATUS_COMPLETE = 'C'
    REPORT_STATUS_FAILED = 'F'

    REPORT_STATUS_CHOICES = [
        (REPORT_STATUS_PENDING, 'Pending'),
        (REPORT_STATUS_COMPLETE, 'Complete'),
        (REPORT_STATUS_FAILED, 'Failed'),
    ]
    status = models.CharField(max_length=1, choices=REPORT_STATUS_CHOICES, default=REPORT_STATUS_PENDING)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    #if user is deleted, delete report? Or keep users always for data analytics?
    user = models.ForeignKey(User, on_delete=CASCADE)

    #Reports can have multiple tags, tags could be assigned to multiple reports
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title