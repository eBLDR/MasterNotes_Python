import uuid

from nameko.rpc import rpc
# Ideally, each microservice would have its own database instance. However,
# for simplicity, a single Redis database is used for microservices to share.
from nameko_redis import Redis


class AirportsService:
    name = 'airports_service'

    redis = Redis('development')

    @rpc
    def get(self, airport_id):
        return self.redis.get(airport_id)

    @rpc
    def create(self, airport):
        airport_id = uuid.uuid4().hex
        self.redis.set(airport_id, airport)

        return airport_id
