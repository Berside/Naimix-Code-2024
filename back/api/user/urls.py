from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import UserAuthViewSet, UserLoggedViewSet

urlpatterns = [
    # Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # UserAuth
    path('api/v1/auth/login/', UserAuthViewSet.as_view({'get': 'login'})),
    path('api/v1/auth/register/', UserAuthViewSet.as_view({'post': 'register'})),
    path('api/v1/auth/logout/', UserLoggedViewSet.as_view({'get': 'logout'})),
    path('api/v1/auth/status/', UserLoggedViewSet.as_view({'get': 'status'})),
]
