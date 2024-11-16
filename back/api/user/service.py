from django.forms import model_to_dict

from user.repository import UserRepository
from astropy.time import Time
from astropy.coordinates import EarthLocation
from user.models import CustomUser
from user.serializers import UserRegisterSerializer, UserGetSerializer, UserUpdateSerializer


class UserService:
    @staticmethod
    def register_user(data: dict) -> None:
        serializer = UserRegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        UserRepository.register_user(data)

    @staticmethod
    def login(email: str, password: str):
        return UserRepository.login(email, password)

    @staticmethod
    def get_one(data: dict) -> UserGetSerializer:
        user = UserRepository.get_one(data)
        data = model_to_dict(user, fields=[field.name for field in user._meta.fields\
                                           if field.name not in ['password', 'last_login', 'is_superuser']])
        return data

    @staticmethod
    def get_many(data: dict):
        users = UserRepository.get_many(data)
        data = []
        for user in users:
            data.append(model_to_dict(user, fields=[field.name for field in user._meta.fields\
                                           if field.name not in ['password', 'last_login', 'is_superuser']]))
        return data

    @staticmethod
    def update(email: str, data: dict):
        # serializer = UserUpdateSerializer(data=data)
        # serializer.is_valid(raise_exception=True)
        # UserRepository.update(email, serializer.validated_data)
        UserRepository.update(email, data)

    @staticmethod
    def delete(email: str):
        UserRepository.delete(email)
