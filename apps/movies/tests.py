import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.users.models import User
from apps.movies.models import Movie


class MovieTestCase(TestCase):
    def setUp(self):
        user = User(email="testing@tests.com", first_name="Testing", last_name="Testing", username="testing")
        user.set_password("12345678910aB@")
        user.save()
        self.user = user

        movie1 = Movie(
            name="Test Name",
            summary="Test summary",
            release_date="2022-02-02",
            directed_by="Mr Nobody",
            running_time=100,
            language="Spanish",
            is_private=True,
            user=self.user,
        )
        movie1.save()

    def test_get_movies(self):
        user = User.objects.get(email="testing@tests.com")
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get("/movies/movies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_movies(self):
        user = User.objects.get(email="testing@tests.com")
        client = APIClient()
        client.force_authenticate(user=user)
        data = {
            "name": "The origin",
            "summary": "Movie about dreams",
            "release_date": "2008-01-01",
            "directed_by": "Martin Scorcese",
            "running_time": 157,
            "language": "English",
            "is_private": True
        }
        response = client.post("/movies/movies/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        result = json.loads(response.content)
        self.assertEqual(result["name"], data["name"])
