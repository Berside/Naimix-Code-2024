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

    @staticmethod
    def get_one(data: dict):
        user = CustomUser.objects.filter(**data)
        return user.first()

    @staticmethod
    def get_many(data: dict):
        users = CustomUser.objects.filter(**data)
        return users

    @staticmethod
    def update(email: str, data: dict):
        CustomUser.objects.filter(email=email).update(**data)

    @staticmethod
    def update_current_user(user_id: int, data:dict):
        CustomUser.objects.filter(id=user_id).update(**data)

    @staticmethod
    def delete(email: str):
        CustomUser.objects.filter(email=email).delete()
