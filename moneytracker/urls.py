from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from cash.views import ActivityViewSet
from moneytracker.views import homepage

router = routers.DefaultRouter()
router.register(r'activity', ActivityViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_auth.urls')),
    path('api-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('cash/', include('cash.urls')),
    path('', homepage, name='homepage'),
]
