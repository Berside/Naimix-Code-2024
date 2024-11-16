from datetime import datetime
from pytz import timezone
import swisseph as swe


class AstrologyService:
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

    def calculate_planet_positions(self, birthdate, latitude, longitude):
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
