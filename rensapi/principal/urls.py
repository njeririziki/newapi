from django.urls import path, include
from rest_framework import  routers
from .views import PrincipalViewSet, DependantsViewSet


router = routers.DefaultRouter()
router.register(r'principal', PrincipalViewSet)
router.register(r'dependants', DependantsViewSet)


urlpatterns = [
    path('', include(router.urls))

   
]