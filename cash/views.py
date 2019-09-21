from django.views.generic import ListView
from rest_framework import viewsets

from cash.models import Activity
from cash.serializers import ActivitySerializer


class MainView(ListView):
    model = Activity
    template_name = 'cash/index.html'


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('-timestamp')
    serializer_class = ActivitySerializer
