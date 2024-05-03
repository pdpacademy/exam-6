from django.contrib.auth.models import User
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    location = models.CharField(max_length=155)
    profession = models.CharField(max_length=155)
    photo = models.ImageField()