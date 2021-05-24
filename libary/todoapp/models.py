from django.db import models
from userapp.models import UserModelSet


class ProjectModelSet(models.Model):
    name = models.CharField(max_length= 128)
    url = models.URLField()
    user = models.ManyToManyField(UserModelSet)

    def __str__(self):
        return self.name

class TodoModelSet(models.Model):
    project = models.ForeignKey(ProjectModelSet, related_name='project',on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='текст',max_length=256, blank=True)
    create = models.DateTimeField(verbose_name='создан',auto_now_add=True)
    update = models.DateTimeField(verbose_name='обновил',auto_now=True)
    user = models.ForeignKey(UserModelSet,related_name='user',on_delete=models.CASCADE)
    active = models.BooleanField(verbose_name='активный',default=True)