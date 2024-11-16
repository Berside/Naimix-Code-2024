from django.db import models
from geopy.geocoders import Nominatim
import requests

from user.models import CustomUser


# Модель для хранения координат планет пользователей
class PlanetPosition(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='planets')
    planet = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f"{self.planet} - {self.longitude}°, {self.latitude}°"

    @staticmethod
    def get_coordinates(user):
        """
        Получает координаты пользователя из адреса рождения.
        
        :param user: CustomUser объект
        :return: tuple (latitude, longitude)
        """
        geolocator = Nominatim(user_agent="horoscope")
        location = geolocator.reverse(f"{user.birth_city}, {user.birth_country}")
        return location.latitude, location.longitude

    def save(self, *args, **kwargs):
        """
        Сохраняет модель и заполняет отсутствующие координаты.
        """
        if not self.longitude or not self.latitude:
            lat, lon = self.get_coordinates(self.user)
            self.longitude = lon
            self.latitude = lat
        super().save(*args, **kwargs)

    def update_position(self):
        """
        Обновляет позицию планеты пользователя.
        """
        lat, lon = self.get_coordinates(self.user)
        self.longitude = lon
        self.latitude = lat
        self.save()


class Aspect(models.Model):
    """
    Модель для представления аспектов между планетами в астрологии.
    
    Аспекты - это геометрические отношения между планетами, которые считаются важными в астрологии.
    Каждый аспект имеет тип, связанные с ним планеты и орбиту (позволяющую определить точность аспекта).
    """
    ASPECT_TYPES = [
        ('TRINE', 'Trigon'),
        ('SQUARE', 'Square'),
        ('CONJUNCTION', 'Conjunction'),
        ('OPPOSITION', 'Opposition'),
        ('SEXTILE', 'Sextile'),
        ('QUINCUNX', 'Quincunx'),
    ]

    type = models.CharField(max_length=20, choices=ASPECT_TYPES)
    planet1 = models.ForeignKey(PlanetPosition, on_delete=models.CASCADE, related_name='aspect1')
    planet2 = models.ForeignKey(PlanetPosition, on_delete=models.CASCADE, related_name='aspect2')
    orb = models.FloatField()

    def __str__(self):
        return f"{self.planet1.planet} {self.type} {self.planet2.planet}"
