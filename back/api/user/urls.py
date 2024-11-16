from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import UserAuthViewSet, UserLoggedViewSet

urlpatterns = [
    # UserAuth
    path('auth/login/', UserAuthViewSet.as_view({'get': 'login'})),
    path('auth/register/', UserAuthViewSet.as_view({'post': 'register'})),
    path('auth/logout/', UserLoggedViewSet.as_view({'get': 'logout'})),
    path('auth/status/', UserLoggedViewSet.as_view({'get': 'status'})),
    path('get_one/', UserLoggedViewSet.as_view({'get': 'get_one'})),
    path('get_many/', UserLoggedViewSet.as_view({'get': 'get_many'})),
    path('update/', UserLoggedViewSet.as_view({'patch': 'update'})),
    path('delete/', UserLoggedViewSet.as_view({'delete': 'delete'})),
]
