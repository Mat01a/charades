from django_redis import get_redis_connection

class RoomService:

    def __init__(self):
        self.redis = get_redis_connection()

    @staticmethod
    def create_room(self, room_id):
        self.redis.sadd("active_rooms", room_id)
    
    @staticmethod
    def delete_room(self, room_id):
        self.redis.srem("active_rooms", room_id)
    
    @staticmethod
    def list_rooms(self):
        return self.redis.smembers("active_rooms")
    