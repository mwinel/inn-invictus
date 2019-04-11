from rest_framework import generics
from .serializer import CommentSerializer
from .models import Comment


class CreateViewComment(generics.ListCreateAPIView):
    """
    View class for the comment model to deal with POST and GET ALL
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ViewComment(generics.RetrieveUpdateDestroyAPIView):
    """
    View class for the comment model to deal with GET ONE, UPDATE ONE AND DELETE ONE
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
