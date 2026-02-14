from django.test import TestCase
from api.repository.redis import Redis

class RepositoryTest(TestCase):
    def setUp(self):
        self.db = Redis("tests")
    
    def test_valid_saving(self):
        """Testing saving function while input is valid"""
        result = self.db.save(f"room:1:state", "active")
        self.assertIsNone(result)

    def test_invalid_params_saving_raises_error(self):
        """Testing saving with invalid input"""
        with self.assertRaises(TypeError) as context:
            invalid_amount_of_params = self.db.save("lack_of_second_argument")
            too_much_params = self.db.save("too","much","arguments")
    
    def test_has_function(self):
        """Testing has function"""
        self.db.save(f"room:1:state", "active")
        has = self.db.has(f"room:1:state", "active")
        self.assertEqual(has, 1)