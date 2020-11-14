from django.shortcuts import render
from django import forms
tasks = ["foo", "", "hello"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task") 
# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks" : tasks
    })
def addtask(request, method = "POST"):
    return render(request, "tasks/addtask.html",{
        "form": NewTaskForm()
    })