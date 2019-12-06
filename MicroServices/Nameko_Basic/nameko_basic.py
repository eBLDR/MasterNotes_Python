# Nameko - Python framework for building microservices
import time

# To use RPC communication protocol
from nameko.rpc import rpc


class BasicService:
    """
    This is a Nameko service, defined as a class.
    These service classes are instantiated at the moment a call is made and
    destroyed after the call is completed. They are inherently stateless.
    The instantiated services are called 'workers'.
    Each running service can instantiate a maximum number of workers (defined
    in the config file), therefore each service is able of handling that same
    number of calls concurrently.
    To simulate service scaling, we can run the service again in another
    process. This will start another service instance with the potential to run
    more workers.
    When there are more than one service instances running, Nameko will
    delegate the RPC requests among the available instances.
    If one service instance is shut down, Nameko will reallocate the calls to
    another available service instance.
    Having several different versions of the same service running at the same
    time is not a problem. Since Nameko distributes the calls in a round-robin
    fashion, the calls might go through old or new versions.
    """
    # Service name
    name = 'basic_service'

    # Nameko classes expose entry points, which are implemented as extensions.
    # The built-in extensions include the ability to create entry points that
    # represent RPC methods, event listeners, HTTP endpoints or timers.
    @rpc
    def hello(self, name):
        return f'Hello, {name}!'

    @rpc
    def concurrent(self):
        # Use 'call_async' method to see concurrent calls working
        call_timestamp = time.time()
        time.sleep(5)
        return f'{time.time():.2f} - Call was made at: {call_timestamp:.2f}.'
