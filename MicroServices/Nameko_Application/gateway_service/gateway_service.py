"""
Manages the HTTP connection with the client through an API exposing endpoints.
And manages the RPC connection between microservices internally.
"""
import json

from nameko.rpc import RpcProxy
# To use HTTP communication protocol
from nameko.web.handlers import http


class GatewayService:
    """
    The Gateway microservice will receive HTTP requests via a simple REST-like
    API and use RPC to communicate with Airports and Trips.
    """
    name = 'gateway_service'

    # Declare the other RPC services
    airports_rpc = RpcProxy('airports_service')
    routes_rpc = RpcProxy('routes_service')

    # Expose HTTP endpoints
    @http('GET', '/airport/<string:airport_id>')
    def get_airport(self, request, airport_id):
        """
        Retrieve airport from database (if exists).
        @request is always passed as first argument.
        """
        # Call method "get()" on RPC service - method must exist
        airport = self.airports_rpc.get(airport_id)

        return json.dumps(
            {
                'airport': airport,
            }
        )

    @http('POST', '/airport')
    def post_airport(self, request):
        """
        Create a new airport key:value into database.
        request body:
            {
                "airport": "<name>"
            }
        """
        # request.get_data() contains the request's JSON string
        data = json.loads(request.get_data(as_text=True))

        if not data.get('airport'):
            return 'JSON data field "airport" is empty.'

        return self.airports_rpc.create(data['airport'])

    @http('GET', '/route/<string:route_id>')
    def get_route(self, request, route_id):
        """
        Retrieve route from database (if exists).
        """
        route = self.routes_rpc.get(route_id)

        return json.dumps(
            {
                'route': route,
            }
        )

    @http('POST', '/route')
    def post_route(self, request):
        """
        Create a new route into database.
        request body:
            {
                "airport_from": "<name>",
                "airport_to": "<name>"
            }
        """
        data = json.loads(request.get_data(as_text=True))

        if not data.get('airport_from') or not data.get('airport_to'):
            return 'JSON data is invalid.'

        return self.routes_rpc.create(
            data['airport_from'],
            data['airport_to'],
        )
