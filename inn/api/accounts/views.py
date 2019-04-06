from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import login
from .serializer import UserSerializer, LoginSerializer
from rest_framework import status
from django.contrib.auth.password_validation import ValidationError


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Login(APIView):
    # queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=serializer.data['username'])
        login(request, user)

        return Response(
            data={"Username": serializer.data['username'],
                  "Email": serializer.data['email'],
                  "token": serializer.data['token']},
            status=status.HTTP_200_OK

        )


class SignUp(APIView):
    serializer_class = UserSerializer
    # queryset = User.objects.all()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
            except ValidationError as errors:
                return Response(
                        data={"status": 400,
                              "errors": [errors]
                              },
                        status=status.HTTP_400_BAD_REQUEST,
                )

            return Response(
                data={
                    "status": status.HTTP_201_CREATED,
                    "data": [
                        {
                            "username": user.username,
                            "email": user.email,
                            "is_admin": user.is_superuser,
                        }
                    ],
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            data={"status": 400, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
