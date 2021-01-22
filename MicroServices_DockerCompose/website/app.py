from flask import Flask
from requests import get

app = Flask(__name__)


@app.route('/')
def index():
    return '''
    <html>
        <head>
            <title>Little Shop</title>
        </head>
        <body>
            <h1>Welcome!</h1>
            <h2>Available:</h2>
            <ul>
                {items_list}
            </ul>
        </body>
    </html>'''.format(
        items_list=''.join([
            f'<li>{item.title()}: {qty}</li>'
            for item, qty in ProductsServiceClient().get_products().items()
        ])
    )


# The following code would usually be in another file
class ProductsServiceClient:
    """
    This app will communicate with products API.
    """

    def __init__(self):
        # Docker-compose created a virtual network among the container, their
        # host name matches their service name.
        self.products_api_url = 'http://products-service'

    def get_products(self):
        # Make a request to products service
        try:
            return get(self.products_api_url).json()
        except ConnectionError:
            return 'Products service is not available.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
