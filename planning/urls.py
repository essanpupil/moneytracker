from django.urls import path

from planning.views import main

app_name = 'planning'
urlpatterns = [
    path('', main, name='main'),
]
