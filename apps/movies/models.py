from django.db import models

from apps.users.models import User


class Movie(models.Model):
    name = models.CharField(max_length=250)
    summary = models.CharField(max_length=250, blank=True, null=True)
    release_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    directed_by = models.CharField(max_length=250, blank=True, null=True)
    running_time = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    is_private = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)


class Character(models.Model):
    actor_name = models.CharField(max_length=250)
    character_name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    is_private = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
