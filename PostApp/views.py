from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Post,Like
from .serializers import PostSerializer,LikeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


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


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    # this method is for update
    def put(self, request, pk, *args, **kwargs):
        return self.update(request, pk, *args, **kwargs)

    # this will create the object in Like table for
    # respective post and user,who has liked the post.
    @action(detail=True, methods=['POST'])
    def likePost(self, request, pk=None):
        post = Post.objects.get(id=pk)
        user = request.user
        try:
            likes = Like.objects.create(user=user, post=post)
        except:
            return Response({'message': 'You have already liked the post'})
        serializer = LikeSerializer(likes, many=False)
        response = {'message': 'Liked Post', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    # this will delete the object in Like table for
    # respective post and user,who has disliked the post.
    @action(detail=True, methods=['DELETE'])
    def dislikePost(self, request, pk=None):
        post = Post.objects.get(id=pk)
        user = request.user
        try:
            likes = Like.objects.get(user=user, post=post)
            likes.delete()
        except Exception:
            return Response({'message': "You haven't liked the post yet."})
        response = {'message': 'Disliked Post so deleted'}
        return Response(response, status=status.HTTP_204_NO_CONTENT)


# queryset : set of all like objects
# serializer_class : present them in a way mentioned in serializers.py
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
