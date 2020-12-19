from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user