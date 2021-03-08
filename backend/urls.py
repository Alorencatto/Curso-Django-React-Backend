
from django.contrib import admin
from rest_framework import routers
from .views import UserViewSet,GroupViewSet

from django.urls import include, path



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
