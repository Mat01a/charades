from django_redis import get_redis_connection
from api.repository.redis import Redis

class GameService:

    def __init__(self, repo):
        self.db = repo
    
    def _handle_error(self, error):
        print(f"Error: {str(error)}")

    def create_room(self, room_id, user):
        self.db.save(f"room:{room_id}:state", "active")
        self.db.save(f"rooms:list", room_id)
        self.db.save(f"room:{room_id}:players", user)
    
    def delete_room(self, room_id):
        self.db.delete(f"room:{room_id}:state", "disactivated")
        self.db.delete(f"rooms:list", room_id)

    
    def list_rooms(self):
        rooms = self.db.get(f"rooms:list")
        return rooms