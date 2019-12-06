import redis

r = redis.Redis(db=1)

my_items = {f'item:{index}': i for index, i in enumerate((
    {
        'value_open': 5,
        'value_close': 1,
    },
    {
        'value_open': 7,
        'value_close': 0,
    },
    {
        'value_open': 3,
        'value_close': 2,
    }
))
            }

"""
'Pipelining' is a way to cut down the number of round-trip transactions that
are needed to write or read data from Redis server. Each operation necessitates
a back-and-forth round trip operation for each row written.
With a pipeline, all the commands are buffered on the client side and then sent
at once, in one fell swoop, when calling pipe.execute().
"""
with r.pipeline() as pipe:
    for item_id, item in my_items.items():
        # Use pipe object instead of Redis instance
        pipe.hmset(item_id, item)

    # Run all piped operations
    # (print call is only for learning purposes)
    print(pipe.execute())

print(r.keys())
print(r.hgetall('item:0'))
