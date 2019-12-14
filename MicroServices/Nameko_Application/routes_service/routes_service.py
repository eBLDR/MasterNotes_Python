"""
Manages the list of routes.
"""
import os
import uuid

from nameko.rpc import rpc
from redis import Redis


class RoutesService:
    name = 'routes_service'

    redis = Redis(host=os.getenv('REDIS_HOST'), decode_responses=True)

    @rpc
    def get(self, route_id):
        return self.redis.hgetall(route_id)

    @rpc
    def create(self, airport_from_id, airport_to_id):
        route_id = uuid.uuid4().hex
        self.redis.hmset(
            route_id,
            {
                'from': airport_from_id,
                'to': airport_to_id,
            }
        )

        return route_id
