from datetime import datetime
import pytz

from horoscope.models import PlanetPosition, Aspect
from user.models import CustomUser


class AstrologyRepository:
    """
    Репозиторий для работы с астрологическими данными.
    
    Этот класс содержит методы для получения профиля пользователя, сохранения позиции планеты
    и создания аспектов между планетами.
    """
    def get_user_profile(self, user_id):
        """
        Получает профиль пользователя по ID.
        
        :param user_id: ID пользователя
        :return: CustomUser объект
        """
        return CustomUser.objects.get(id=user_id)

    def save_planet_position(self, user, planet_name, longitude):
        """
        Создает новую запись позиции планеты для пользователя.
        
        :param user: CustomUser объект
        :param planet_name: Название планеты
        :param longitude: Долгота позиции планеты
        """
        PlanetPosition.objects.create(
            user=user,
            planet=planet_name,
            longitude=longitude
        )

    def save_aspect(self, aspect):
        """
        Создает новый аспект между двумя планетами.
        
        :param aspect: Словарь с данными аспекта:
                       {
                           'type': тип аспекта,
                           'planet1': связанный объект PlanetPosition,
                           'planet2': связанный объект PlanetPosition,
                           'orb': точность аспекта в градусах
                       }
        """
        Aspect.objects.create(
            type=aspect['type'],
            planet1=aspect['planet1'],
            planet2=aspect['planet2'],
            orb=aspect['orb']
        )
