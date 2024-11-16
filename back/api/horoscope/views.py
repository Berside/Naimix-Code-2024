from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from horoscope.service import AstrologyService
from horoscope.repository import AstrologyRepository


class HoroscopeViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
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
        return Response(context)


class CountSynastryViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        id_1 = request.data.get('id_1')
        id_2 = request.data.get('id_2')
        
        repository = AstrologyRepository()
        service = AstrologyService()

        user1 = repository.get_user_profile(id_1)
        user2 = repository.get_user_profile(id_2)
        
        compatibility = service.calculate_compatibility(user1, user2)
        
        return Response({'compatibility': compatibility})


class NatalChartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        id = request.query_params.get('id')
        
        repository = AstrologyRepository()
        service = AstrologyService()

        user = repository.get_user_profile(id)
        
        birth_date = user.birthdate
        latitude = user.latitude
        longitude = user.longitude
        
        planets = service.calculate_planet_positions(birth_date, latitude, longitude)
        
        return Response({
            'birth_date': birth_date,
            'latitude': latitude,
            'longitude': longitude,
            'planets': [{'name': planet['name'], 'longitude': planet['longitude']} for planet in planets]
        })


class SynastryViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        id_1 = request.query_params.get('id_1')
        id_2 = request.query_params.get('id_2')
        
        repository = AstrologyRepository()
        service = AstrologyService()

        user1 = repository.get_user_profile(id_1)
        user2 = repository.get_user_profile(id_2)
        compatibility = service.calculate_compatibility(user1, user2)
        return Response({'compatibility': compatibility})
