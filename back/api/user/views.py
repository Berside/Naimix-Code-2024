from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from user.service import UserService
from .serializers import UserSerializer
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
        print(request.query_params)
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
