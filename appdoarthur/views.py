from django.shortcuts import render, redirect
from .models import Task, Champ

def home(request):
  champs = Champ.objects.all()
  tasks = Task.objects.all()
  context = {'champs': champs,"tasks":tasks}
  return render(request, 'home.html', context)
  
def list_tasks(request):
  tasks = Task.objects.all()
  context = {"tasks":tasks}
  return render(request,"list_tasks.html", context=context)
  
def list_champs(request):
  champ = Champ.objects.all()
  context = {"champs":champ}
  return render(request,"list_champs.html", context=context)

def create_task(request):
  if request.method == "POST":
    if "done" not in request.POST:
      done=False
    else:
      done=True
    Task.objects.create(
      title=request.POST["title"],
      description=request.POST["description"],
      due_date=request.POST["due-date"],
      done=done
    )
    return redirect("list_tasks")
  return render(request,"task_form.html")

def create_champ(request):
  if request.method == "POST":
    Champ.objects.create(
      campeão=request.POST["champ"],
      função=request.POST["function"],
      posição=request.POST["posicao"],
      tipo=request.POST["tipo"]
    )
    return redirect("list_champs")
  return render(request,"champs_form.html")

def update_task(request,task_id):
  task = Task.objects.get(id = task_id)
  task.due_date = task.due_date.strftime("%Y-%m-%d")
  if request.method == "POST":
    task.title=request.POST["title"]
    task.description=request.POST["description"]
    task.due_date=request.POST["due-date"]
    if "done" not in request.POST:
      task.done=False
    else:
      task.done=True
    task.save()
    return redirect("list_tasks")
  context={"task":task}
  print(type (task.due_date))
  return render(request,"task_form.html",context=context)

def delete_task(request,task_id):
  task = Task.objects.get(id=task_id)
  if request.method == "POST":
    if "confirm" in request.POST:
      task.delete()
    return redirect("list_tasks")
  context={"task":task}
  return render(request,"delete_form.html",context=context)

def update_champ(request,champ_id):
  champ = Champ.objects.get(id=champ_id)
  if request.method == "POST":
    champ.campeão=request.POST["champ"]
    champ.função=request.POST["function"]
    champ.posição=request.POST["posicao"]
    champ.tipo=request.POST["tipo"]
    champ.save()
    return redirect("list_champs")
  context={"champ":champ}
  return render(request,"champs_form.html",context=context)

def delete_champ(request,champ_id):
  champ = Champ.objects.get(id=champ_id)
  if request.method == "POST":
    if "confirm" in request.POST:
      champ.delete()
    return redirect("list_champs")
  context={"champ":champ}
  return render(request,"delete_champ_form.html",context=context)
