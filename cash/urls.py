from django.urls import path

from cash.views import MainView, NewActivity

app_name = 'cash'
urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('new', NewActivity.as_view(), name='new'),
]