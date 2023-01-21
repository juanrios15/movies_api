from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import MovieSerializer, CharacterSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MovieSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CharacterSerializer
