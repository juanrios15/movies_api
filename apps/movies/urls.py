from django.urls import path, include
from rest_framework import routers

from .views import MovieViewSet, CharacterViewSet

app_name = "movies"

router = routers.DefaultRouter()

router.register(r"movies", MovieViewSet, basename="movies")
router.register(r"characters", CharacterViewSet, basename="characters")

urlpatterns = [
    path("", include(router.urls)),
]
