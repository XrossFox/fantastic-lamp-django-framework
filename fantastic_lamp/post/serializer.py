from rest_framework.serializers import ModelSerializer
from post.models import Post

class CreatePostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'content', 'date']