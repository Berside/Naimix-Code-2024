# from user.models import User, AdditionalUserInfo


# class UserRepository:
#     @staticmethod
#     def register_user(login, password, birthdate=None,
#                       birth_country=None, birth_city=None,
#                       first_name=None, last_name=None, middle_name=None):
#         return User.objects.create_user(
#             login=login,
#             password=password,
#             birthdate=birthdate,
#             birth_country=birth_country,
#             birth_city=birth_city,
#             first_name=first_name,
#             last_name=last_name,
#             middle_name=middle_name
#         )

#     @staticmethod
#     def get_user_by_login(login):
#         return User.objects.filter(login=login).first()

#     @staticmethod
#     def get_user_additional_info(user_id):
#         return AdditionalUserInfo.objects.get(user_id=user_id)

#     @staticmethod
#     def save_user_additional_info(user_id, additional_info):
#         info, _ = AdditionalUserInfo.objects.get_or_create(user_id=user_id)
#         info.additional_info = additional_info
#         info.save()
from user.models import CustomUser
from typing import Optional

from user.serializers import UserSerializer


# from pydantic import BaseModel, Field
# from pydantic_settings import Settings

# settings = Settings(".env")

# class UserCreateRequest(BaseModel):
#     login: str
#     password: str
#     birthdate: Optional[str] = None
#     birth_country: Optional[str] = None
#     birth_city: Optional[str] = None
#     first_name: Optional[str] = None
#     last_name: Optional[str] = None
#     middle_name: Optional[str] = None

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
