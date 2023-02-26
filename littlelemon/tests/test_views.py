from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
import json
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.test import TestCase

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='lauren', email="lauren@littlelemon.com", password="testpassword")
        T = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + T.key)
        Menu.objects.create(title = "thai fish", price=16, inventory=20)
        Menu.objects.create(title = "papaya", price =2, inventory=10)

    def test_getall(self):
        items = MenuSerializer(Menu.objects.all(), many= True).data
        url = reverse("menu")
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), items)

