from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import HoroscopeViewSet, CountSynastryViewSet, NatalChartViewSet, SynastryViewSet

router = DefaultRouter()
router.register(r'horoscope', HoroscopeViewSet, basename='horoscope')
router.register(r'count-synastry', CountSynastryViewSet, basename='count-synastry')
router.register(r'notal-chart', NatalChartViewSet, basename='notal-chart')
router.register(r'synastry', SynastryViewSet, basename='synastry')

urlpatterns = [
    path('', include(router.urls)),
]
