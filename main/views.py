from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", {"basestyle":"root/style.css"})

# def greet(request, name):
#     return HttpResponse(f"Hello, {name}!")
