from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
