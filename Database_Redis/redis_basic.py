"""
Methods in module redis-py are invoked in the same way as Redis CLI commands.
In general, methods return True if they were success, and False otherwise.
Accepted key types are: bytes, str, int, float - redis-py will convert them to
bytes before sending them to Redis server.
"""
import redis

# Instantiating a Redis client - Redis() is the central class
# Redis(@host='localhost', @port=6379, @db=0, @password=None, ...)
# @db specifies the database number - each DB is independent
r = redis.Redis()
# The TCP socket connection and reuse is done behind the scenes

# Test connection
print(r.ping())

# Set new key-value pair
r.set('my_key', 'my_value')

# Get the value
v = r.get('my_key')
print(v, type(v))  # Bytes type

# Convert to str if desired
v = v.decode('utf-8')
print(v, type(v))

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

