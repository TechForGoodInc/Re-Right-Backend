from django.shortcuts import render

from .models import Report
from .serializers import ReportDetailSerializer
from .serializers import ReportListSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def report_overview(request):
    api_urls = {
        'List': '/report-list/',
        'Detail': '/report-detail/<str:pk>/',
        'Create': '/report-creation/',
        # 'Edit': '/report-edit/<str:pk>/',
        'Delete': '/report-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def report_list(request):
    reports = Report.objects.all().only('title')
    serializer = ReportListSerializer(reports, many=True)
    return Response(serializer.data)

@api_view(['GET'])
#Not yet sure how authentication works
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def report_detail(request, pk):
    report = Report.objects.get(id=pk)
    serializer = ReportDetailSerializer(report, many=False)
    return Response(serializer.data)

@api_view(['POST'])
#Not yet sure how authentication works
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def report_create(request):
    serializer = ReportDetailSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# @api_view(['POST'])
# def report_edit(request, pk):
#     report = Report.objects.get(id=pk)
#     serializer = ReportDetailSerializer(instance = report, data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

@api_view(['DELETE'])
#Not yet sure how authentication works
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def report_delete(request, pk):
    report = Report.objects.get(id=pk)
    report.delete()
    return Response("Report Deleted")
