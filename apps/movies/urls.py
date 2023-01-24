from django.urls import path, include
from rest_framework import routers

from .views import MovieViewSet

app_name = "movies"

router = routers.DefaultRouter()

router.register(r"movies", MovieViewSet, basename="movies")

urlpatterns = [
    path("", include(router.urls)),
]
