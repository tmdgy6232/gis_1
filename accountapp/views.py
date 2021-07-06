from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def helloworld(request):
    return render(request, 'accountapp/hello_world.html')