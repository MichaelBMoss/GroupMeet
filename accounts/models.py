from django.db import models
from django.contrib.auth.models import User


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

class Interests_m(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    interest1 = models.CharField(max_length=127)
    interest2 = models.CharField(max_length=127)
    interest3 = models.CharField(max_length=127)
    interest4 = models.CharField(max_length=127)
    interest5 = models.CharField(max_length=127)
    user = models.CharField(max_length=127, default='No Name')
    email = models.CharField(max_length=127, default='No Email')
