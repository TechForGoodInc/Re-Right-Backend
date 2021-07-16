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
# Create your views here.

posts = [
    {'title': 'My First Post',
     'body': 'just my first post, hi!',
     'date_created': 'July 16, 2021',
     'author': 'Mary Sue',
     'no_of_likes': 0,
     'no_of_comments': 0}
]
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'put', 'delete']
    permission_classes = [IsAuthenticated]


def post_creation(request):
    return HttpResponse('<h1> Post Creation Page </h1>')