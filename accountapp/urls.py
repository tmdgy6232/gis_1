from django.urls import path, include

from accountapp.views import helloworld, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', helloworld, name = 'hello_world'),
    path('create/', AccountCreateView.as_view(), name='create')
]