from django.shortcuts import render

tasks = ["foo", "", "hello"]
# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks" : tasks
    })