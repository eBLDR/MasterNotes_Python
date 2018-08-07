#! /usr/bin/python3

"""
Will run a web application on a local server.

http://127.0.0.1:<port>/ is equivalent to localhost:<port>

!! URLs are case sensitive !!
"""

from flask import Flask

# Creating an instance of a web application
# (__name__) will take "__main__" if the module is the main execution
app = Flask(__name__)


# VIEW FUNCTION
# When client request a given URL, the corresponding function is executed
# argument is the route (URL) - which can be anything we want
@app.route('/')
@app.route('/index')  # more than one web address can redirect to the same function
def index():
    # function to be executed when the route is accessed

    # data to be returned - in HTML
    # return "Hello, World!"  # by default <p>'content'</p>

    # a full HTML code can be returned as a string
    return '''
<html>
    <head>
        <title>Home Page - Demo Flask App</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
    </body>
</html>'''


if __name__ == '__main__':
    # debug mode to trace possible errors
    # host and port can also be manually defined, by default host is
    # localhost and port is 5000 (127.0.0.1:5000)
    app.run(debug=True, host='127.0.0.1', port=5000)
