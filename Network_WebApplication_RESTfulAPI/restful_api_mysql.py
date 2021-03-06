from flask import Flask
# reqparse module for parsing arguments
from flask_restful import Api, Resource, reqparse
# Importing flask-mysql connector
from flaskext.mysql import MySQL

# Flask instance
app = Flask(__name__)

# MySQL instance
db = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'bldr'
app.config['MYSQL_DATABASE_PASSWORD'] = 'free'
# Using the database created in Database_MySQL notes
app.config['MYSQL_DATABASE_DB'] = 'UsersDb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# Initialising db
db.init_app(app)

# Api instance
api = Api(app)


# API endpoint - inherits from Resource class
class CreateUser(Resource):
    # POST request
    @staticmethod
    def post():
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()  # Creating parser - dictionary like

            # Adding arguments to the parser
            parser.add_argument('email', type=str, help='Email address to create user')
            parser.add_argument('password', type=str, help='Password to create user')

            # Extracting the arguments into variables
            args = parser.parse_args()
            _user_email = args['email']
            _user_password = args['password']

            conn = db.connect()
            cursor = conn.cursor()

            # Calling the procedure declared inside the MySQL database
            cursor.callproc('spCreateUser', (_user_email, _user_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StatusCode': '200', 'Message': 'User creation success'}
            else:
                return {'StatusCode': '1000', 'Message': str(data[0])}

            # For testing
            # return {'status': 'success'}
            # return {'Email': _user_email, 'Password': _user_password}

        except Exception as e:
            return {'error': str(e)}

    # Testing get method
    @staticmethod
    def get():
        return 'Hello'


# Hooking up the CreateUser class to the /createuser endpoint
api.add_resource(CreateUser, '/createuser')

if __name__ == '__main__':
    app.run(debug=True)
