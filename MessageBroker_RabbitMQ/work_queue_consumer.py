"""
This is a consumer - receives messages.
Before running this python script, RabbitMQ server must be running.

In a work queue (aka task queue) each message is delivered to exactly one
worker. To simulate a work queue, create few consumers and start producing
messages.
"""
from time import sleep

import pika

QUEUE_NAME = 'simple_queue'

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='127.0.0.1',
        port=5672,
    )
)

channel = connection.channel()

# Create a queue with the same name as the producer, whoever runs it first,
# it will actually create the queue. queue_declare() is idempotent - it can be
# run multiple times that only one queue will be created.
# Queue names must be unique, and is not possible to redefine an existing queue
# with different parameters.
channel.queue_declare(queue=QUEUE_NAME, durable=True)


# To receive a message, the consumer needs to subscribe a callback function to
# the queue. Whenever the consumers receives a message, the callback function
# is called.
def callback(channel_, method, properties, body):
    """
    :param channel_: pika channel
    :param method: pika deliver method
    :param properties: pika properties
    :param body: <bytes>, actual message
    """
    # print(type(channel_))
    # print(type(method), method)
    # print(type(properties))
    # print(type(body))  # Binary
    print(f'Consumer received: {body}')

    # Simulate some task
    sleep(body.count(b'.') * 2)

    print('Done.')

    # Send acknowledgement
    channel_.basic_ack(delivery_tag=method.delivery_tag)


# By default, RabbitMQ dispatches a message when the message enters the queue,
# dispatching it to the next consumer in the sequence.
# Setting the following option, tells the broker not to give more than one
# message to the worker (consumer) at a time. So the broker won't dispatch a
# new message to the worker until it as processed and acknowledged the
# previous one.
channel.basic_qos(prefetch_count=1)

# Subscribe the callback function to a particular queue - queue must exist.
channel.basic_consume(
    queue=QUEUE_NAME,
    # auto_ack=True,  # This disables the manual acknowledgement.
    on_message_callback=callback,  # Subscribe callback function.
)

"""
Manual acknowledgement:
An acknowledgement is sent back by the consumer to tell the broker that a
particular message had been received, processed and that the broker is free to
delete it.
If a consumer dies (its channel is closed, connection is closed, or TCP
connection is lost) without sending an ack, the broker will understand that a
message wasn't processed fully and will re-queue it. Making sure that no
message is lost.
Manual acknowledgements are turned on by default.
"""

print('Waiting for messages...')

# Enter a loop that waits for data and runs callbacks upon receiving a message.
channel.start_consuming()
