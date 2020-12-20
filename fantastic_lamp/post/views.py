from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from post.models import Post
from post.serializer import CreatePostSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.contrib.auth.models import User


# Create your views here.

class CreatePost(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        currentUserPk = User.objects.get(username=request.user).pk
        body = {
            "author": currentUserPk,
            "content": request.data.get("content"),
            "date": datetime.now()
        }

        serializer = CreatePostSerializer(data=body)

        if serializer.is_valid():
            serializer.save()
            print(serializer.validated_data)
            return Response("Post created", status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)