from django.urls import path

from cash.views import MainView

app_name = 'cash'
urlpatterns = [
    path('', MainView.as_view(), name='main'),
]
