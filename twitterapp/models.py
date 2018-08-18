
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.


class Tweet(models.Model):
    content = models.CharField(max_length=200)
    creation_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=getattr()self.user.last_name)



