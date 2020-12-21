from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from post.models import Post
from post.serializer import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.contrib.auth.models import User


# Create your views here.

class CreatePost(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        currentUserPk = User.objects.get(username=request.user).pk
        body = {
            "author": currentUserPk,
            "content": request.data.get("content"),
            "date": datetime.now()
        }

        serializer = PostSerializer(data=body)

        if serializer.is_valid():
            serializer.save()
            print(serializer.validated_data)
            return Response("Post created", status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListPost(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeletePost(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, format=None):
        try:
            post = Post.objects.get(pk=pk)
            if post.author.pk == User.objects.get(username=request.user).pk:
                post.delete()
                return Response("Deleted succesfully", status=status.HTTP_204_NO_CONTENT)
            return Response("Cannot delete this post, you are not the owner", status=status.HTTP_304_NOT_MODIFIED)
        except Exception as e:
            return Response("Post not found", status=status.HTTP_404_NOT_FOUND)
