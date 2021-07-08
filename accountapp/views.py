from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def helloworld(request):
    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html', context={'text' : 'PostMethod'})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text' : 'getMethod'})
