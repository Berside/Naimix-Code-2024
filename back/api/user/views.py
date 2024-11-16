from django.forms import model_to_dict
from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from user.service import UserService
from .serializers import UserSerializer, UserGetSerializer, UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token

from user.serializers import UserRegisterSerializer


class UserAuthViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @staticmethod
    @extend_schema(
        request=UserRegisterSerializer,
        responses={200: JsonResponse},
    )
    def register(request):
        UserService.register_user(request.data)
        return JsonResponse({"message": "success"})

    @staticmethod
    def login(request):
        email = request.query_params.get('email')
        password = request.query_params.get('password')
        if email and password:
            user = UserService.login(email, password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({
                    'token': token.key,
                    'message': 'Login successful',
                })
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=401)
        return JsonResponse({'message': 'invalid data'})


class UserLoggedViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @staticmethod
    @extend_schema(
        request=None,
        responses={200: UserSerializer},
    )
    def logout(request):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            return JsonResponse({'message': 'Logged out successfully'})
        return JsonResponse({'message': 'User is not Authorized'})

    @staticmethod
    def status(request):
        return JsonResponse({'message': 'hello'})

    @staticmethod
    def get_current_user(request):
        user = request.user
        data = model_to_dict(user, fields=[field.name for field in user._meta.fields \
                                           if field.name not in ['password', 'last_login', 'is_superuser']])
        return JsonResponse(data)

    @staticmethod
    @extend_schema(
        # parameters=UserGetSerializer,
        responses={200: UserGetSerializer},
    )
    def get_one(request):
        data = UserService.get_one(request.query_params.dict())
        return JsonResponse(data)

    @staticmethod
    @extend_schema(
        # parameters=UserGetSerializer,
        responses={200: UserGetSerializer},
    )
    def get_many(request):
        data = UserService.get_many(request.query_params.dict())
        return JsonResponse(data, safe=False)

    @staticmethod
    @extend_schema(
        # parameters=UserUpdateSerializer,
        responses={200: UserGetSerializer},
    )
    def update(request):
        data = request.data
        email = data['email']
        del data['email']
        if email:
            UserService.update(email, data)
            return JsonResponse({'message': 'success'})
        return JsonResponse({'error': 'wrong email'})

    @staticmethod
    @extend_schema(
        # parameters=UserGetSerializer,
        responses={200: UserGetSerializer},
    )

    def update_current_user(request):
        data = request.data
        UserService.update_current_user(request.user.id, data)
        return JsonResponse({'message': 'success'})

    def delete(request):
        email = request.data['email']
        if email:
            UserService.delete(email)
            return JsonResponse({'message': 'success'})
        return JsonResponse({'error': 'wrong email'})
