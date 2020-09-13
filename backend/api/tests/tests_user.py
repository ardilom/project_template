# django
from django.urls import reverse

# models
from backend.api.models import User

# django rest
from rest_framework.test import APITestCase


class OKUserCreationTestCase(APITestCase):

    def setUp(self):
        self.name = "Test"
        self.last_name = "User"
        self.email = "testuser@gmail.com"
        self.password = "testuser"

    def test_create_user(self):
        user = User.objects.create_superuser(
            email=self.email,
            password=self.password,
            first_name=self.name,
            last_name=self.last_name
        )
        self.assertIsNotNone(user, msg="Null!")
