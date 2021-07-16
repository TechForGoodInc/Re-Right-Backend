from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

posts = [
    {'title': 'My First Post',
     'body': 'just my first post, hi!',
     'date_created': 'July 16, 2021',
     'author': 'Mary Sue',
     'no_of_likes': 0,
     'no_of_comments': 0}
]

def post_creation(request):
    return HttpResponse('<h1> Post Creation Page </h1>')