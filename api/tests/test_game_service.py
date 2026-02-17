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
        self.service.handle_user(room_id=1, user='test')


    def test_handling_multiple_users_joining_same_room(self):
        """Test if you can try to join multiple users an room"""
        self.service.handle_user(room_id=2, user='test2')
        self.service.handle_user(room_id=2, user='test3')

