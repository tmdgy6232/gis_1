from django.urls import path, include

from accountapp.views import helloworld

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', helloworld, name = 'hello_world'),
]