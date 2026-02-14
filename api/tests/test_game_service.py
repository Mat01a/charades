from django.test import TestCase
from unittest.mock import Mock
from api.repository.redis import Redis

from api.services.game_service import GameService


class GameServiceTest(TestCase):

    def setUp(self):
        self.db = Redis("tests")
        self.service = GameService(repo=self.db)


    def test_create_game_room(self):
        """Test creating room"""
        self.service.create_room(room_id=1, user='test')


    def test_create_game_room_duplicates(self):
        """Test if you can try to create an room with existing room_id"""
        self.service.create_room(room_id=2, user='test2')
        with self.assertRaises(ValueError) as context:
            self.service.create_room(room_id=2, user='test3')
        self.assertEqual(str(context.exception), "Room with that id exists")

