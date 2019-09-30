from django.shortcuts import render
from rest_framework import viewsets

from cash.models import Activity
from cash.serializers import ActivitySerializer


def main(request):
    return render(request, 'cash/index.html')


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('-timestamp')
    serializer_class = ActivitySerializer
