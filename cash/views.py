from django.views.generic import ListView

from cash.models import Activity


class MainView(ListView):
    model = Activity
    template_name = 'cash/index.html'
