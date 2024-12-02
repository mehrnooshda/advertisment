from user.models import AdUser
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from .models import Ad, Comment


class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = AdUser.objects.create_user(
            email='testuser@example.com',
            username='testuser@example.com',
            password='password123'
        )
        self.client.force_authenticate(user=self.user)  # Authenticate the user
        self.ad = Ad.objects.create(title="Test Ad", description="Test Description", owner=self.user)


    def test_create_ad(self):
        data = {"title": "New Ad", "description": "Ad Description"}
        response = self.client.post('/ads/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Ad")

    def test_get_ads(self):
        response = self.client.get('/ads/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)  # Ensure at least one ad is returned

    def test_update_ad(self):
        data = {"title": "Updated Title"}
        response = self.client.patch(f'/ads/{self.ad.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Title")

    def test_delete_ad(self):
        response = self.client.delete(f'/ads/{self.ad.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

