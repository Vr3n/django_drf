from rest_framework import serializers
from .models import Post

class PostSerialier(serializers.ModelSerializer):
    """Serializing the Post Model into JSON api."""
    class Meta:
        model = Post
        fields = [
            'title', 'description', 'owner'
        ]