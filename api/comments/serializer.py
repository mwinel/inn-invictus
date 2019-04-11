from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer class for the comment model
    """
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ('created_on')

        
