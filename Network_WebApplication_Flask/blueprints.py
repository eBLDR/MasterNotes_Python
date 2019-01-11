"""
A flask blueprint is a way to organize flask app into smaller apis.
It also defines a collection of views, templates and assets.
All blueprint files should be inside a subdirectory called 'api' inside our flask app directory.

To use a blueprint, from the main Flask app file, we need to register it:

from api.my_api import api

And after app = Flask(__name__) creation

app.register_blueprint(api)
"""

# Class import
from flask import Blueprint
from flask import request

# Instance - @api_name, @name_of_package, @url_prefix
api = Blueprint('my_api', __name__, url_prefix='/api')


# The api can be treated now like a normal flask app
# Sample route


# Since api has a prefix set to /api, the route will be concatenated, being /api/test
@api.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        return 'POST OK'
    else:
        return 'GET OK'
