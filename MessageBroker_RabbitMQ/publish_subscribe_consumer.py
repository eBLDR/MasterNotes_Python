"""
In a publish/subscribe (aka pub/sub) queue, a single message is delivered
to multiple consumers (as opposed to a work queue).
"""
import pika

EXCHANGE_NAME = 'simple_exchange'

connection = pika.BlockingConnection(
    pika.ConnectionParameters()
)

channel = connection.channel()

# Declare the exchange to which the consumer wants to subscribe.
channel.exchange_declare(
    exchange=EXCHANGE_NAME,
    exchange_type='fanout',
)

# Declare a temporary queue, as for pub/sub we are not interested in the queue
# itself, rather we want to listen to the exchange - one queue is created for
# each subscriber.
queue = channel.queue_declare(
    queue='',  # The server chooses a random queue name.
    exclusive=True,  # The queue will be deleted once the connection is closed.
)

# Get queue name
queue_name = queue.method.queue
print(f'Queue name is: {queue_name}')

# The relationship between exchange and a queue is a "binding". This tells to
# the exchange to send messages to the given queue.
channel.queue_bind(
    exchange=EXCHANGE_NAME,
    queue=queue_name,
    # routing_key='my_key',  # Add this binding key to get from exchange ONLY
    # those messages that have that routing key as well. Requires a "direct"
    # exchange type.
)


def callback(ch, method, properties, body):
    print(f'Consumer received: {body}')


channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True,
)

print('Waiting for messages...')

channel.start_consuming()
