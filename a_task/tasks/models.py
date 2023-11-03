from django.db import models


# Create your models here.
class Task(models.Model):
    summary = models.CharField(max_length=100, verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Описание')

