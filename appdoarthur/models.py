from django.db import models #Importa o módulo models do pacote django.db

class Task(models.Model): #Define o modelo de uma Task com título, descrição, data de entrega, e uma checkbox de conclusão
  title = models.CharField(max_length=50)
  description = models.TextField()
  due_date = models.DateField()
  done = models.BooleanField()

class Champ(models.Model): #Define o modelo de um Champ com nome do campeão, função, posição e tipo
  campeão = models.CharField(max_length=50)
  função = models.TextField()
  posição = models.CharField(max_length=50)
  tipo = models.CharField(max_length=50)
