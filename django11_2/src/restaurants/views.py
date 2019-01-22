import random
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    num = random.randint(0, 1000)
    names = ["Bob", "Jennifer"]
    context = {"name": "John", "num": num, "names": names}
    return render(request, "base.html", context)
