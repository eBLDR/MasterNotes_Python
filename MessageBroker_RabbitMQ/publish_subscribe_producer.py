import sys

import pika

EXCHANGE_NAME = 'simple_exchange'

msg_body = ' '.join(sys.argv[1:]) or 'Hi all!'

connection = pika.BlockingConnection(
    pika.ConnectionParameters()
)

channel = connection.channel()

# Create an exchange
channel.exchange_declare(
    exchange=EXCHANGE_NAME,
    exchange_type='fanout',  # fanout exchange type: broadcasts all the
    # messages it receives to all the queues it knows.
)

channel.basic_publish(
    exchange=EXCHANGE_NAME,
    routing_key='',  # @routing_key (mandatory) - allows to add a filter to the
    # messages, enabling the exchange to send messages selectively - empty str
    # to set it without filters (sending to all bind queues). Selective
    # message sending requires exchange_type='direct' in exchange_declare().
    body=msg_body,
)

print(f'Producer sent: {msg_body}')

connection.close()
