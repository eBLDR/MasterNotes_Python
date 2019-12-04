import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:
    """
    The Gateway microservice will receive HTTP requests via a simple REST-like
    API and use RPC to communicate with Airports and Trips.
    """
    name = 'gateway'

    airports_rpc = RpcProxy('airports_service')
    trips_rpc = RpcProxy('trips_service')

    @http('GET', '/airport/<string:airport_id>')
    def get_airport(self, request, airport_id):
        """
        @request is always passed as first argument.
        """
        airport = self.airports_rpc.get(airport_id)

        return json.dumps(
            {
                'airport': airport,
            }
        )

    @http('POST', '/airport')
    def post_airport(self, request):
        # request.get_data() contains the request's JSON string
        data = json.loads(request.get_data(as_text=True))

        if not data.get('airport'):
            return 'JSON data field "airport" is empty.'

        return self.airports_rpc.create(data['airport'])

    @http('GET', '/trip/<string:trip_id>')
    def get_trip(self, request, trip_id):
        trip = self.trips_rpc.get(trip_id)

        return json.dumps(
            {
                'trip': trip,
            }
        )

    @http('POST', '/trip')
    def post_trip(self, request):
        data = json.loads(request.get_data(as_text=True))

        if not data.get('airport_from') or not data.get('airport_to'):
            return 'JSON data is invalid.'

        return self.trips_rpc.create(
            data['airport_from'],
            data['airport_to'],
        )
