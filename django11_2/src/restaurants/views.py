import random
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    num = random.randint(0, 1000)
    names = ["Bob", "Jennifer"]
    context = {"name": "John", "num": num, "names": names}
    return render(request, "home.html", context)


def contact(request):
    return render(request, "contact.html", {})


def about(request):
    return render(request, "about.html", {})
