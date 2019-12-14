"""
Methods in module redis-py are invoked in the same way as Redis CLI commands.
Accepted key types are: bytes, str, int, float - redis-py will convert them to
bytes before sending them to Redis server.
"""
from time import sleep

import redis

# Instantiating a Redis client - Redis() is the central class.
# Redis(@host='localhost', @port=6379, @db=0, @password=None, ...)
# @db specifies the database number - each DB is independent.
# Note: do not specify the protocol in @host.
# If @decode_responses argument is set to True, all redis values will be
# decoded using @charset (utf-8 by default).
r = redis.Redis()
# The TCP socket connection and reuse is done behind the scenes.

# Test connection
print(r.ping())

# Set new key-value pair
r.set('my_key', 'my_value')

# Check if a key exists
print(r.exists('my_key'))

# Get the value
v = r.get('my_key')
print(v, type(v))  # Bytes type

# Convert to str if desired
v = v.decode('utf-8')
print(v, type(v))

print('#' * 20)

# Setting many from dict
r.mset(
    {
        'key_1': 1,
        'key_2': 2,
     }
)

print(r.mget('key_1', 'non-existing'))

# Display all keys - !! careful on big DB
print(r.keys())

print('#' * 20)

# Add expiry time to a key
sample_key = 'key_1'
print(r.exists(sample_key))

# See time left - in seconds
print(r.ttl(sample_key))

# Set expiry in seconds from current timestamps
r.expire(sample_key, 2)  # timedelta object can also be used as argument

# Set expiry at given time
# r.expireat(@key, @datetime)

print(r.ttl(sample_key))

sleep(3)
print(r.exists(sample_key))

# Set a key with expiry time
r.setex('new_key', 1, 'short lived')  # psetex() - time in milliseconds
print(r.pttl('new_key'))  # pttl display time left in milliseconds
print(r.pttl('new_key'))
print(r.pttl('new_key'))
