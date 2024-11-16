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

class UserGetSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'telephone', 'birthdate', 'birth_country', 'birth_city',
                  'first_name', 'last_name', 'middle_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make all fields optional
        for field in self.fields.values():
            field.required = False


class UserUpdateSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'birthdate', 'birth_country', 'birth_city',
                  'first_name', 'last_name', 'middle_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make all fields optional
        for field in self.fields.values():
            field.required = False
