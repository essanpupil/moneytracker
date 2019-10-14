from django.urls import path

from cash.views import main

app_name = 'cash'
urlpatterns = [
    path('', main, name='main'),
]
