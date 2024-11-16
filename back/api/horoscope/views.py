from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from horoscope.service import AstrologyService
from horoscope.repository import AstrologyRepository


class BaseViewSet(viewsets.ViewSet):
    """
    Базовый класс для всех ViewSet'ов в проекте.
    
    Обеспечивает общую логику и методы, используемые всеми дочерними классами.
    """
    permission_classes = [IsAuthenticated]

    def _get_users(self, request):
        """
        Получает профили пользователей из запроса.
        
        :param request: HTTP-запрос с параметрами запроса
        :return: ТUPLE с профилами пользователей
        """
        id_1 = request.query_params.get('id_1')
        id_2 = request.query_params.get('id_2')
        repository = AstrologyRepository()
        return repository.get_user_profile(id_1), repository.get_user_profile(id_2) if id_2 else None

    def _calculate_compatibility(self, user1, user2):
        """
        Вычисляет совместимость между двумя пользователями.
        
        :param user1: Профиль первого пользователя
        :param user2: Профиль второго пользователя (может быть None)
        :return: Результат вычисления совместимости
        """
        service = AstrologyService()
        return service.calculate_compatibility(user1, user2)


class HoroscopeViewSet(BaseViewSet):
    """
    API для получения гороскопа пользователя.
    """
    def list(self, request):
        """
        Получает гороскоп пользователя по его ID.
        
        :param request: HTTP-запрос
        :return: JSON-ответ с гороскопом пользователя
        """
        repository = AstrologyRepository()
        service = AstrologyService()

        user = repository.get_user_profile(request.query_params.get('id'))
        planet_positions = service.calculate_planet_positions(
            user.birthdate,
            user.latitude,
            user.longitude
        )

        for position in planet_positions:
            repository.save_planet_position({
                'user': user.id,
                'planet': position['name'],
                'longitude': position['longitude'],
                'latitude': position['latitude']
            })

        aspects = service.calculate_aspects(planet_positions)
        for aspect in aspects:
            repository.save_aspect(aspect)

        interpreted_aspects = [service.interpret_aspect(aspect) for aspect in aspects]
        summary = service.summarize_compatibility(user, user)
        context = {
            'user': user.id,
            'aspects': [{'type': aspect['type'], 'planet1': aspect['planet1'], 'planet2': aspect['planet2'], 'orb': aspect['orb'], 'interpretation': interpretation} for aspect, interpretation in zip(aspects, interpreted_aspects)],
            'summary': summary,
        }
        return JsonResponse(context)


class CountSynastryViewSet(BaseViewSet):
    """
    API для подсчета совместимости двух пользователей.
    
    Предоставляет метод для создания синастрии двух пользователей.
    """
    def create(self, request):
        """
        Создает синастрию между двумя пользователями.
        
        :param request: HTTP-запрос с ID обоих пользователей
        :return: JSON-ответ с результатами синастрии
        """
        user1, user2 = self._get_users(request)
        compatibility = self._calculate_compatibility(user1, user2)
        
        return JsonResponse({
            'compatibility': compatibility,
            'users': {
                'user1': user1.id,
                'user2': user2.id if user2 else None
            }
        })


class NatalChartViewSet(BaseViewSet):
    """
    API для получения натальского гороскопа пользователя.
    
    Предоставляет метод для получения информации о положении планет
    на момент рождения пользователя.
    """
    def retrieve(self, request, pk=None):
        """
        Получает натальский гороскоп пользователя по его ID.
        
        :param request: HTTP-запрос с ID пользователя
        :param pk: Не используется (обязательный параметр для ViewSet)
        :return: JSON-ответ с информацией о положении планет
        """
        id = request.query_params.get('id')
        repository = AstrologyRepository()
        service = AstrologyService()

        user = repository.get_user_profile(id)
        
        birth_date = user.birthdate
        latitude = user.latitude
        longitude = user.longitude
        
        planets = service.calculate_planet_positions(birth_date, latitude, longitude)
        
        return JsonResponse({
            'birth_date': birth_date,
            'latitude': latitude,
            'longitude': longitude,
            'planets': [{'name': planet['name'], 'longitude': planet['longitude']} for planet in planets]
        })


class SynastryViewSet(BaseViewSet):
    """
    API для получения синастрии двух пользователей.
    
    Предоставляет метод для сравнения гороскопов двух пользователей.
    """
    def retrieve(self, request, pk=None):
        """
        Получает синастрию между двумя пользователями.
        
        :param request: HTTP-запрос с ID обоих пользователей
        :param pk: Не используется (обязательный параметр для ViewSet)
        :return: JSON-ответ с результатами синастрии
        """
        user1, user2 = self._get_users(request)
        compatibility = self._calculate_compatibility(user1, user2)
        return JsonResponse({'compatibility': compatibility})
