from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from cash.views import ActivityViewSet
from moneytracker.views import homepage, dashboard

router = routers.DefaultRouter()
router.register(r'cash/activity', ActivityViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    path('cash/', include('cash.urls')),
    path('planning/', include('planning.urls')),

    path('dashboard/', dashboard, name='dashboard'),
    path('', homepage, name='homepage'),
]
