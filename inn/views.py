from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializer import UserSerializer


@api_view(['GET', ])
def Home(request):
    content = {'message': 'My Hello, World App!'}
    return Response(content)


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
