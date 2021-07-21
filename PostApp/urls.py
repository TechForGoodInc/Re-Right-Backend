from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_overview, name="post_overview"),
    path('post-list/', views.post_list, name="post_list"),
    path('post-detail/<str:pk>', views.post_detail, name="post_detail"),
    path('post-creation/', views.post_create, name="post_creation"),
    path('post-edit/<str:pk>', views.post_edit, name="post_edit"),
    path('post-delete/<str:pk>', views.post_delete, name="post_delete"),
]