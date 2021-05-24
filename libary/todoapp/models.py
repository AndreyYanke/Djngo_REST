from django.db import models
from userapp.models import UserModelSet


class ProjectModelSet(models.Model):
    name = models.CharField(max_length= 128)
    url = models.URLField()
    user = models.ManyToManyField(UserModelSet)

    def __str__(self):
        return self.name

class TodoModelSet(models.Model):
    project = models.ForeignKey(ProjectModelSet, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ManyToManyField(UserModelSet)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
