import redis

r = redis.Redis(db=1)

hats = {f'hat:{index}': i for index, i in enumerate((
    {
        'color': 'black',
        'price': 49.99,
        'style': 'fitted',
        'quantity': 1000,
        'npurchased': 0,
    },
    {
        'color': 'maroon',
        'price': 59.99,
        'style': 'hipster',
        'quantity': 500,
        'npurchased': 0,
    },
    {
        'color': 'green',
        'price': 99.99,
        'style': 'baseball',
        'quantity': 200,
        'npurchased': 0,
    }))
}


def purchase(hat_id):
    pass
