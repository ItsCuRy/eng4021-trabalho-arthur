from django.db import models

class Task(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  due_date = models.DateField()
  done = models.BooleanField()

class Champ(models.Model):
  campeão = models.CharField(max_length=50)
  função = models.TextField()
  posição = models.CharField(max_length=50)
  tipo = models.CharField(max_length=50)