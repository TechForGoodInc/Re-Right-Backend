from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_overview, name="report_overview"),
    path('report-list/', views.report_list, name="report_list"),
    path('report-detail/<str:pk>', views.report_detail, name="report_detail"),
    path('report-creation/', views.report_create, name="report_creation"),
    # path('report-edit/<str:pk>', views.report_edit, name="report_edit"),
    path('report-delete/<str:pk>', views.report_delete, name="report_delete"),
]