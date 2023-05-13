from django.contrib import admin #Importa o módulo admin do pacote django.contrib 
from .models import Task #Importa a função Task do arquivo .models 
from .models import Champ #Importa a função Champ do arquivo .models

admin.site.register(Task) #Registra o modelo Task para gerenciamento dos registros no admin do site
admin.site.register(Champ) #Registra o modelo Champ para gerenciamento dos reistros no admin do site
