from django_redis import get_redis_connection

class Redis:

    def __init__(self, type):
        self.connection = get_redis_connection(type)

    def save(self, set_key, members):
        self.connection.sadd(set_key, members)

    def get(self, members):
        results = self.connection.smembers(members)
        return results
