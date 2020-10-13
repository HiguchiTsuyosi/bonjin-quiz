from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    question=models.TextField()
    answer=models.BooleanField()
    comment=models.TextField()