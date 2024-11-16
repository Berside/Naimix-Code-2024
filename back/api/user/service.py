from user.repository import UserRepository
from astropy.time import Time
from astropy.coordinates import EarthLocation
from user.models import CustomUser
from user.serializers import UserRegisterSerializer


class UserService:
    @staticmethod
    def register_user(data: dict) -> None:
        serializer = UserRegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        UserRepository.register_user(data)

    @staticmethod
    def login(email: str, password: str):
        return UserRepository.login(email, password)
