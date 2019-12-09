import uuid

from nameko.rpc import rpc
from nameko_redis import Redis


class RoutesService:
    name = 'routes_service'

    redis = Redis('development')

    @rpc
    def get(self, route_id):
        route = self.redis.get(route_id)
        return route

    @rpc
    def create(self, airport_from_id, airport_to_id):
        route_id = uuid.uuid4().hex
        self.redis.set(
            route_id,
            {
                'from': airport_from_id,
                'to': airport_to_id,
            }
        )

        return route_id
