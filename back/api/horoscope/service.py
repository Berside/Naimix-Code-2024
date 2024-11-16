from datetime import datetime
from django.core.cache import cache
from pytz import timezone
import swisseph as swe

from user.models import CustomUser


class AstrologyService:
    """
    Сервис для расчета астрологических аспектов и совместимости пользователей.
    
    Этот класс содержит методы для расчета позиции планет,
    аспектов между ними и оценки совместимости пользователей.
    """
    def __init__(self):
        self.PLANETS = {
            'Sun': swe.SUN,
            'Moon': swe.MOON,
            'Mercury': swe.MERCURY,
            'Venus': swe.VENUS,
            'Mars': swe.MARS,
            'Jupiter': swe.JUPITER,
            'Saturn': swe.SATURN,
            'Uranus': swe.URANUS,
            'Neptune': swe.NEPTUNE,
            'Pluto': swe.PLUTO,
            'Ascendant': swe.ASC,
            'Midheaven': swe.MC,
        }

        self.ASPECTS = {
            'CONJUNCTION': 0,
            'SEXTILE': 60,
            'SQUARE': 90,
            'TRINE': 120,
            'OPPOSITION': 180,
            'QUINCUNX': 45,
        }

        self.MAX_ORB = {
            'CONJUNCTION': 8,
            'SEXTILE': 6,
            'SQUARE': 8,
            'TRINE': 8,
            'OPPOSITION': 8,
            'QUINCUNX': 3,
        }

        self.ASPECT_INTERPRETATIONS = {
            'CONJUNCTION': {
                'positive': 'Усиление влияния планет, гармония.',
                'negative': 'Может создавать напряжение из-за смешения энергий.'
            },
            'SEXTILE': {
                'positive': 'Возможности для сотрудничества и роста.',
                'negative': 'Требует усилий для реализации потенциала.'
            },
            'SQUARE': {
                'positive': 'Триггер для роста и преодоления препятствий.',
                'negative': 'Конфликты и напряжение.'
            },
            'TRINE': {
                'positive': 'Гармония и легкость взаимодействия.',
                'negative': 'Может приводить к ленивости из-за чрезмерной гармонии.'
            },
            'OPPOSITION': {
                'positive': 'Баланс и понимание противоположностей.',
                'negative': 'Конфликты и противоречия.'
            },
            'QUINCUNX': {
                'positive': 'Адаптация и гибкость.',
                'negative': 'Неловкость и необходимость изменений.'
            },
        }
        self.KEY_ASPECTS = {
            'CONJUNCTION': 'favorable',
            'TRINE': 'favorable',
            'SQUARE': 'tension',
            'OPPOSITION': 'tension',
            'SEXTILE': 'neutral',
            'QUINCUNX': 'neutral',
        }

    def calculate_planet_positions(self, birthdate, latitude, longitude):
        """
        Расчитывает позиции планет для заданной даты и координат.
        
        :param birthdate: Дата рождения пользователя
        :param latitude: Широта
        :param longitude: Долгота
        :return: Список словарей с информацией о планетах
        """
        dt = birthdate
        jd = swe.julday(dt.year, dt.month, dt.day, dt.hour + dt.minute / 60.0)

        planet_positions = []
        for name, code in self.PLANETS.items():
            if name in ['Ascendant', 'Midheaven']:
                pos = swe.houses(jd, latitude, longitude)[0][0] if name == 'Ascendant' else swe.houses(jd, latitude, longitude)[1][0]
            else:
                pos, _ = swe.calc_ut(jd, code)
                pos = pos[0]
            planet_positions.append({'name': name, 'longitude': pos})

        return planet_positions

    def calculate_aspects(self, planets):
        """
        Вычисляет аспекты между планетами.
        
        :param planets: Список словарей с информацией о планетах
        :return: Список словарей с информацией об аспектах
        """
        aspects = []
        for i in range(len(planets)):
            for j in range(i + 1, len(planets)):
                p1 = planets[i]
                p2 = planets[j]
                angle = abs(p1['longitude'] - p2['longitude'])
                angle = angle if angle <= 180 else 360 - angle
                for aspect, degree in self.ASPECTS.items():
                    orb = abs(angle - degree)
                    if orb <= self.MAX_ORB[aspect]:
                        aspects.append({
                            'type': aspect,
                            'planet1': p1['name'],
                            'planet2': p2['name'],
                            'orb': orb
                        })
        return aspects

    def interpret_aspect(self, aspect):
        """
        Интерпретирует аспект с учетом его природы (положительной или отрицательной).
        
        :param aspect: Словарь с информацией об аспекте
        :return: Интерпретация аспекта
        """
        interpretation = self.ASPECT_INTERPRETATIONS.get(aspect['type'], {})
        positive_aspects = ['CONJUNCTION', 'SEXTILE', 'TRINE']
        negative_aspects = ['SQUARE', 'OPPOSITION', 'QUINCUNX']

        if aspect['type'] in positive_aspects:
            nature = 'positive'
        elif aspect['type'] in negative_aspects:
            nature = 'negative'
        else:
            nature = 'neutral'                 
        return interpretation.get(nature, 'No interpretation available.')
    
    def calculate_compatibility(self, user1, user2):
        """
        Оценивает совместимость между двумя пользователями.
        
        :param user1: Первый пользователь
        :param user2: Второй пользователь
        :return: Коэффициент совместимости
        """
        aspects1 = self.calculate_aspects(user1.planets.all())
        aspects2 = self.calculate_aspects(user2.planets.all())

        compatibility_score = 0.0
        for asp1 in aspects1:
            for asp2 in aspects2:
                if asp1['type'] == asp2['type']:
                    compatibility_score += (self.MAX_ORB[asp1['type']] - asp1['orb']) + (self.MAX_ORB[asp2['type']] - asp2['orb'])

        compatibility_score = compatibility_score / (len(aspects1) + len(aspects2))
        return compatibility_score

    def categorize_aspect(self, aspect):
        """
        Категоризирует аспект как благоприятный, напряженный или нейтральный.
        
        :param aspect: Словарь с информацией об аспекте
        :return: Категория аспекта
        """
        category = self.KEY_ASPECTS.get(aspect.type, 'neutral')
        return category
    
    def summarize_compatibility(self, user1, user2):
        """
        Подсчитывает количество благоприятных, напряженных и нейтральных аспектов между пользователями.
        
        :param user1: Первый пользователь
        :param user2: Второй пользователь
        :return: Словарь с суммаризацией аспектов и коэффициентом совместимости
        """
        aspects1 = self.calculate_aspects(user1)
        aspects2 = self.calculate_aspects(user2)
        
        favorable = 0
        tense = 0
        neutral = 0
        
        for asp in aspects1 + aspects2:
            category = self.categorize_aspect(asp)
            if category == 'favorable':
                favorable += 1
            elif category == 'tension':
                tense += 1
            elif category == 'neutral':
                neutral += 1
        
        summary = {
            'favorable_aspects': favorable,
            'tense_aspects': tense,
            'neutral_aspects': neutral,
        }

        compatibility_score = favorable - tense
        summary['compatibility_score'] = compatibility_score
        
        return summary
    
    def get_cached_compatibility(self, user_id_1, user_id_2):
        """
        Получает кэшированный коэффициент совместимости между пользователями.
        
        Использует Django cache для оптимизации производительности.
        
        :param user_id_1: ID первого пользователя
        :param user_id_2: ID второго пользователя
        :return: Словарь с суммаризацией аспектов и коэффициентом совместимости
        """
        cache_key = f"compatibility_{user_id_1}_{user_id_2}"
        result = cache.get(cache_key)
        if result is None:
            user1 = CustomUser.objects.get(id=user_id_1)
            user2 = CustomUser.objects.get(id=user_id_2)
            result = self.summarize_compatibility(user1, user2)
            cache.set(cache_key, result, timeout=3600)
        return result
