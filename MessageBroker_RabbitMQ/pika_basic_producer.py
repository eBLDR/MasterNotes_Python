"""
Pika is a RabbitMQ python client.
This is a producer - sends messages.
Before running this python script, RabbitMQ server must be running.
"""
import sys

import pika

QUEUE_NAME = 'simple_queue'

# Get message from command line
msg_body = ' '.join(sys.argv[1:]) or 'All is good.'

# Establishing connection to RabbitMQ
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='127.0.0.1',  # By default
        port=5672,  # By default
    )
)

channel = connection.channel()

# If a message is sent to a non-existing location, RabbitMQ will just drop the
# message. Declare a queue using queue_declare().
channel.queue_declare(queue=QUEUE_NAME, durable=True)
"""
Setting a queue as "durable" tells the broker to persist message to disk.
Meaning that, even if the broker crashes, queues and messages are not lost.
"""

# To delete a queue
# channel.queue_delete(queue='queue-name')

# Sending a message to a queue. Messages pass first through an exchange.
channel.basic_publish(
    exchange='',  # Default special exchange - which allows to specify to which
    # queue the message should go.
    routing_key=QUEUE_NAME,
    body=msg_body,
    properties=pika.BasicProperties(
        delivery_mode=2,  # Marks the message as persistent - queue must be
        # durable for it to work
    ),
)

print(f'Producer sent: {msg_body}')

# Closing connection to make sure network buffers are flushed.
connection.close()
