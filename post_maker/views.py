from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.



@api_view(['GET'])
def post_overview(request):
    api_urls = {
        'List': '/post-list/',
        'Detail': '/post-detail/<str:pk>/',
        'Create': '/post-creation/',
        'Edit': '/post-edit/<str:pk>/',
        'Delete': '/post-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def post_create(request):
    serializer = PostSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def post_edit(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance = post, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return Response("Post Deleted")

