import redis

r = redis.Redis(db=1)

salutations = (
    ('GER', 'hail'),
    ('EN', 'hello'),
    ('HA', 'aloha'),
    ('ES', 'hola'),
)

"""
'Pipelining' is a way to cut down the number of round-trip transactions that
are needed to write or read data from Redis server. Normally, each operation
necessitates a back-and-forth round trip to server.
With a pipeline, all the commands are buffered on the client side and then sent
at once, in one fell swoop, when calling pipe.execute(). So only one round trip
is made.
"""
with r.pipeline() as pipe:
    for key, value in salutations:
        # Use pipe object instead of Redis instance
        pipe.set(key, value)

    # Run all piped operations
    # (print call is only for learning purposes)
    print(pipe.execute())

print(r.keys())
print(r.get('HA'))
