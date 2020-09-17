from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Entry(models.Model):

    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)