from user.models import CustomUser
from typing import Optional

class UserRepository:
    @staticmethod
    def register_user(data: dict) -> None:
        CustomUser.objects.create_user(data)

    @staticmethod
    def login(email: str, password: str) -> Optional[CustomUser]:
        user = CustomUser.objects.filter(email=email).first()
        if user.check_password(password):
            return user
        return None
