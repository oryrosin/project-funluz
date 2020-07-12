import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from project.models import Activity
from project.serializers import ActivitySerializer

from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase

class ActivityTests(APITestCase):
    urlpatterns = [
        path('api/', include('api.urls')),
    ]

    def test_create_activities(self):
        """
        Ensure we can create a new activity object.
        """
        url = reverse('activities')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        