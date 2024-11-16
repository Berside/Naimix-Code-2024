from django.urls import path

from .views import UserAuthViewSet, UserLoggedViewSet

urlpatterns = [
    # UserAuth
    path('auth/login/', UserAuthViewSet.as_view({'get': 'login'})),
    path('auth/register/', UserAuthViewSet.as_view({'post': 'register'})),
    path('auth/logout/', UserLoggedViewSet.as_view({'get': 'logout'})),
    path('auth/status/', UserLoggedViewSet.as_view({'get': 'status'})),
]
