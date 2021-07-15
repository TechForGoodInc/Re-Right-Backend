from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_creation, name="post_creation"),
]