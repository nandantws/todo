from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from todo.models import Todo


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class ToDoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        exclude = ('created_by',)

    def create(self, validated_data):
        # validated_data["created_by"] = self.context["request"].user
        validated_data["created_by"] = User.objects.all().first()
        return super().create(validated_data)
