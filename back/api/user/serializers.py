from rest_framework import serializers

from user.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'birthdate', 'birth_country', 'birth_city',
                  'first_name', 'last_name', 'middle_name']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'birthdate', 'birth_country', 'birth_city',
                  'first_name', 'last_name', 'middle_name', 'telephone']
