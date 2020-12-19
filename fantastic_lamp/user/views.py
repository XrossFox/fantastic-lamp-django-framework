from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer
from rest_framework import status


# Create your views here.

class CreateNewUser(APIView):
    """
    API View for creating new users
    """
    def post(self, request, format=None):

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response("User Created Succesfully", status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
