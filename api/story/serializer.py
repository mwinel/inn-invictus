from rest_framework import serializers
from .models import Story


class StorySerializer(serializers.ModelSerializer):
    """
    Serializer class for the story model
    """
    class Meta:
        model = Story
        fields = ('id', 'story_title', 'created_on', 'story_body',
                  'author')
        


