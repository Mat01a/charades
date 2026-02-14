from django_redis import get_redis_connection

class Redis:

    def __init__(self):
        self.connection = get_redis_connection()

    def save(self, where, what):
        self.connection.sadd(where, what)

    def get(self, what):
        results = self.connection.smembers(what)
        return results
