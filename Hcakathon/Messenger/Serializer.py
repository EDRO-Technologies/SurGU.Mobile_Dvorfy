from rest_framework import serializers
from .models import User, Task, groups, message

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["name", "email", "password"]

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        field = ["name", "description", "users"]

class GroupsSerializer(serializers.ModelSerializer):

    class Meta:
        model = groups
        field = ["task_id", "id"]

class MessengeSerializer(serializers.ModelSerializer):

    class Meta:
        model = message
        field = ["id", "datatime", "addressee", "destination", "content"]




class RegistrationSerializer(serializers.ModelSerializer):
    """ Сериализация регистрации пользователя и создания нового. """

    # Убедитесь, что пароль содержит не менее 8 символов, не более 128,
    # и так же что он не может быть прочитан клиентской стороной
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    # Клиентская сторона не должна иметь возможность отправлять токен вместе с
    # запросом на регистрацию. Сделаем его доступным только на чтение.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        # Перечислить все поля, которые могут быть включены в запрос
        # или ответ, включая поля, явно указанные выше.
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        # Использовать метод create_user, который мы
        # написали ранее, для создания нового пользователя.
        return User.objects.create_user(**validated_data)