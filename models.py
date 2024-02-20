from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)

class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)



