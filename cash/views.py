from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from cash.models import Activity


class MainView(ListView):
    model = Activity
    template_name = 'cash/index.html'


class NewActivity(CreateView):
    success_url = reverse_lazy('cash:main')
    model = Activity
    template_name = 'cash/new_activity.html'
    fields = '__all__'
