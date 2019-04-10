from rest_framework import generics
from .serializer import StorySerializer
from .models import Story


class CreateViewStory(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class ViewStory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
