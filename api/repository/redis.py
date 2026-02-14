from django_redis import get_redis_connection

class Redis:

    def __init__(self, type="default"):
        self.connection = get_redis_connection(type)

    def save(self, set_key, members):
        self.connection.sadd(set_key, members)

    def get(self, members):
        results = self.connection.smembers(members)
        return results
    
    def has(self, set_key, member):
        return self.connection.sismember(set_key, member)