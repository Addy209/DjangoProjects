from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include


router=DefaultRouter()
router.register('postVS',GenericPostDB)

urlpatterns = [
    path('GVS/', include(router.urls))
    
]