from django.test import TestCase
from django.urls import reverse
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.test import APITestCase
from games.models import GameCategory


class GameCategoryTests(APITestCase):
    def create_game_category(self, name):
        url = reverse('gamecategory-list')
        data = {'name': name}
        response = self.client.post(url, data, format='json')
        return response

    def test_create_and_retrieve_game_category(self):
        new_game_category_name = 'New Game Category'
        response = self.create_game_category(new_game_category_name)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GameCategory.objects.count(), 1)
        self.assertEqual(
            GameCategory.objects.get().name,
            new_game_category_name
        )
        print("PK {0}".format(GameCategory.objects.get().pk))

    def test_create_duplicated_game_category(self):
        url = reverse('gamecategory-list')
        new_game_category_name = 'New Game Category'
        data = {'name': new_game_category_name}
        response1 = self.create_game_category(new_game_category_name)
        self.assertEqual(
            response1.status_code,
            status.HTTP_201_CREATED
        )
        response2 = self.create_game_category(new_game_category_name)
        self.assertEqual(
            response2.status_code,
            status.HTTP_400_BAD_REQUEST
        )




