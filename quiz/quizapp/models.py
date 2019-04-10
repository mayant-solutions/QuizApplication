from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Quiz(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField()


class Questions(models.Model):
    q_no = models.IntegerField('Question No', primary_key=True)
    q_text = models.TextField('Question text', max_length=500)


