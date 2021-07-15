from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from .views import UserViewset, registration_view

router = routers.DefaultRouter()

router.register('users', UserViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', registration_view),
]
