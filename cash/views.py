from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import viewsets

from cash.models import Activity
from cash.serializers import ActivitySerializer


@login_required
def main(request):
    return render(request, 'cash/index.html')


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('-timestamp')
    serializer_class = ActivitySerializer
