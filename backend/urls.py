
from django.contrib import admin
from rest_framework import routers
from .views import UserViewSet,GroupViewSet
from core.views import ListViewSet, ItemViewSet,Teste

from django.urls import include, path

from rest_framework.authtoken import views 

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'list', ListViewSet, basename="list")
router.register(r'item', ItemViewSet)
router.register(r'teste', Teste, basename="teste")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/',views.obtain_auth_token,name='api-tokn-auth'),


]
