from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import status

from todo.models import Todo
from todo.serializers import ToDoSerializer, UserSerializer
from .utils import get_tokens_for_user


# Create your views here.
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "message": "User Created Successfully.",
            "user": UserSerializer(
                user, context=self.get_serializer_context()).data,
            "token": get_tokens_for_user(user)
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response(
                get_tokens_for_user(user), status=status.HTTP_200_OK)
        return Response(
            {'message': 'Invalid Credentials'},
            status=status.HTTP_400_BAD_REQUEST)


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (AllowAny,)

    # permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     user = User.objects.get(id=self.request.user.id)
    #     return Todo.objects.filter(created_by=user)


