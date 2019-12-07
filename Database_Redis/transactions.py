import time

import redis

r = redis.Redis(db=2)


class OutOfStockError(Exception):
    """Raised when certain item is no longer available."""


def purchase_item(r_: redis.Redis, item_id: str) -> None:
    # pipeline() is a transactional pipeline by default.
    with r_.pipeline() as pipe:
        error_count = 0

        while True:
            try:
                # Monitor for changes related to this key before the
                # transaction - if the key is modified by another client from
                # this point until the execute() call, a WatchError will be
                # raised.
                pipe.watch(item_id)

                # Get available inventory.
                n_left: bytes = r.hget(item_id, 'quantity')

                if n_left > b'0':
                    # This is the transaction block itself.
                    pipe.multi()

                    # Operations defined here are buffered, and run atomically
                    # only at the end of the transaction block.
                    pipe.hincrby(item_id, 'quantity', -1)
                    pipe.hincrby(item_id, 'purchased', 1)

                    # To simulate the optimistic locking effect, sleep here
                    # and modify key from another redis client.
                    time.sleep(20)

                    # End of transaction block, send all operations to server.
                    # On execute() call, key is automatically unwatched.
                    pipe.execute()
                    break

                else:
                    # Stop watching the key and raise to break out.
                    pipe.unwatch()
                    raise OutOfStockError(
                        f'Sorry, {item_id} is out of stock!'
                    )

            except redis.WatchError:
                # Key was modified by another client while watching it.
                # Try the same process again.
                error_count += 1
                print(f'WatchError {error_count}: {item_id}; retrying.')

            return None


hats = {f'hat:{index}': i for index, i in enumerate((
    {
        'color': 'black',
        'price': 49.99,
        'style': 'fitted',
        'quantity': 10,
        'purchased': 0,
    },
    {
        'color': 'maroon',
        'price': 59.99,
        'style': 'hipster',
        'quantity': 5,
        'purchased': 0,
    },
    {
        'color': 'green',
        'price': 99.99,
        'style': 'baseball',
        'quantity': 2,
        'purchased': 0,
    }))
        }

# Add hats to server
for hat_id, hat in hats.items():
    r.hmset(hat_id, hat)

print(r.keys())

sample_key = 'hat:2'
print(r.hgetall(sample_key))

for _ in range(3):
    print('Buying...')

    try:
        purchase_item(r, sample_key)
    except OutOfStockError as e:
        print(e)
        break

    print(r.hgetall(sample_key))
