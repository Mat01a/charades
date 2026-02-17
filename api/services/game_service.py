from django_redis import get_redis_connection
from api.repository.redis import Redis

class GameService:

    def __init__(self, repo):
        self.db = repo


    def _handle_error(self, error):
        print(f"Error: {str(error)}")


    def handle_user(self, room_id, user):
        if self.db.has("rooms:list", room_id):
            self.join_room(room_id, user)
            return

        self.create_room(room_id, user)


    def create_room(self, room_id, user):
        self.db.save(f"room:{room_id}:state", "active")
        self.db.save("rooms:list", room_id)
        self.db.save(f"room:{room_id}:players", user)
        self.db.save(f"room:{room_id}:admins", user)
        return True


    def join_room(self, room_id, user):
        self.db.save("rooms:list", room_id)
        self.db.save(f"room:{room_id}:players", user)


    def delete_room(self, room_id):
        self.db.delete(f"room:{room_id}:state", "disactivated")
        self.db.delete("rooms:list", room_id)


    def list_rooms(self):
        rooms = self.db.get("rooms:list")
        return rooms
