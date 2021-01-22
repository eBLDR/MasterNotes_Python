"""
Manages the list of airports.
"""
import os
import uuid

from nameko.rpc import rpc
# Ideally, each microservice would have its own database instance. However,
# for simplicity, a single Redis database is used for microservices to share.
from redis import Redis


class AirportsService:
    name = 'airports_service'

    redis = Redis(host=os.getenv('REDIS_HOST'), decode_responses=True)

    @rpc
    def get(self, airport_id):
        return self.redis.get(airport_id)

    @rpc
    def create(self, airport_name):
        airport_id = uuid.uuid4().hex
        self.redis.set(airport_id, airport_name)

        return airport_id
