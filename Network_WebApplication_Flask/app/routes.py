"""
Here we define the different application routes (URL).
The handler for the app routes are functions, called VIEW FUNCTIONS.
"""
# From app package import object called app
from app import app
# Authorizations
from app.authorization import *
from flask import Response  # To use responses
from flask import json  # To make data conversion
# Function for rendering HTML templates, redirecting and retrieving url associated to a function
from flask import redirect, render_template, url_for
from flask import request  # To use requests methods


# Different endpoints can ping to the same function
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'BLDR'}  # mock user - for testing

    posts = [
        {'author': {'username': 'Ojka'},
         'body': 'Epic training today!'},
        {'author': {'username': 'Coca'},
         'body': '11km in 20 minutes!'}
    ]

    # render_template invokes Jinja2 template engine (bundled with Flask)
    # placeholder - the {{ ... }} fields in the HTML file will be replaced by the arguments
    # @html_file, named_arguments to be replaced in template, if any
    return render_template('index.html', title='Home', user=user, posts=posts)


# <argument> can be used to send arguments to the function's parameters
# A placeholder can be used to control any url combination
# Arguments take the least priority, e.g.: /index will call index() first
# to avoid confusion, converters can be used (it's string by default):
# <int:id>, <float:id>, <path:id>
@app.route('/<num>')
def number(num):
    return 'This is ' + str(num)


# flask's redirect function redirects to desired URL
@app.route('/redirect')
def redirect_():
    # url_for will return a str containing the URL bound to the function passed
    return redirect(url_for('index'))

    # equivalent to redirect('/index')


# ----- REQUESTS -----
# Get parameter
@app.route('/hello')
def api_hello():
    # Send get parameters using /hello?name=myName&age=myAge
    # request.args is a dictionary like with all the parameters
    print(type(request.args))
    # If we need to update the dictionary, use
    print(request.args.to_dict())

    if 'name' in request.args and 'age' in request.args:
        return 'Hello ' + request.args['name'] + ', your age is ' + request.args['age']
    else:
        return 'Hello nobody'


# Request methods - HTTP verbs
@app.route('/echo', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    # User requests (python package) to test the different methods
    return 'ECHO: {}'.format(request.method)


@app.route('/message', methods=['POST'])
def api_message():
    """
    The client sends data to the server.
    """

    if request.headers['Content-Type'] == 'text/plain':
        # Data sent is stored in request.data
        return 'Text message: ' + request.data
    elif request.headers['Content-Type'] == 'application/json':
        return 'JSON message: ' + json.dumps(request.json)
    else:
        return '415 Unsupported Media Type'


# ----- RESPONSES -----
@app.route('/response', methods=['GET'])
def api_response():
    """
    The server sends back data to the client.
    """

    data = {
        'hello': 'world',
        'number': 12
    }

    js = json.dumps(data)
    # (@data, @status_code (200 by default), @data_type)
    resp = Response(response=js, status=200, mimetype='application/json')

    # Using jsonify to simplify syntax, returns exactly the same flask-Response object
    # from flask import jsonify
    # resp = jsonify(data)
    # resp.status_code = 200

    return resp


# ----- ERRORS -----
# Decorator for handling different code errors
# It can only take as argument an Exception type object
@app.errorhandler(404)  # 404 not found error
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }  # request.url return a string of the request's url
    from flask import jsonify
    resp = jsonify(message)
    resp.status_code = 404

    return resp


# ----- AUTHORIZATION -----
@app.route('/secrets')
@requires_auth  # Calling function that handles authorizations
def api_secret():
    return 'Shhh this is top secret spy stuff!'
