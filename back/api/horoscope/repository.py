from horoscope.models import PlanetPosition, Aspect
from user.models import CustomUser
from datetime import datetime
import pytz


class AstrologyRepository:
    def get_user_profile(self, user_id):
        return CustomUser.objects.get(id=user_id)

    def save_planet_position(self, user, planet_name, longitude):
        PlanetPosition.objects.create(
            user=user,
            planet=planet_name,
            longitude=longitude
        )

    def save_aspect(self, aspect):
        Aspect.objects.create(
            type=aspect['type'],
            planet1=aspect['planet1'],
            planet2=aspect['planet2'],
            orb=aspect['orb']
        )
