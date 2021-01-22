from flask import Flask, request
from flask_restful import Api, Resource
from redis import Redis

app = Flask(__name__)
api = Api(app)

PRODUCTS = ['banana', 'apple', 'chocolate']


class Products(Resource):
    def get(self):
        return get_products(), 200

    def post(self):
        """
        Refills stock of all items.
        """
        json_data = request.json

        if not json_data.get('quantity'):
            return 'Invalid JSON', 204

        refill_stock(json_data['quantity'])
        return 'OK', 201


class Product(Resource):
    def get(self, name):
        return get_product(name), 200

    def patch(self, name):
        quantity = get_product(name)

        if quantity in [b'0', '0', 0]:
            return 'Sorry, out of stock.'

        purchase_item(name)
        return 'OK', 202


api.add_resource(Products, '/')
api.add_resource(Product, '/product/<name>')

# Following code would usually be in another file
# @host does not need "http://", as redis automatically adds it.
redis = Redis(host='database-service', port=6379)


def get_product(key):
    value = redis.get(key)
    if not value:
        return '0'

    return value.decode('utf-8')


def get_products():
    return {
        key: get_product(key) for key in PRODUCTS
    }


def refill_stock(quantity):
    for key in PRODUCTS:
        redis.incrby(key, quantity)


def purchase_item(key):
    redis.decrby(key, 1)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
