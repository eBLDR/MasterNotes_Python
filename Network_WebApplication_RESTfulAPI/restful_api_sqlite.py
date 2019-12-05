#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Creating the flask app
app = Flask(__name__)

# Path of the database
DB_PATH = 'testdb.sqlite'

# Setting db's uri
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_PATH

# Disabling track modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Binding SQLAlchemy to flask app
db = SQLAlchemy(app)


# ORM - Binding table
class Asimov(db.Model):
    # Creating table structure
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    year = db.Column(db.String(4))

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def to_dictionary(self):
        tmp = {}
        for i in self.__table__.columns:
            tmp[i.name] = getattr(self, i.name)
        return tmp


# -- ENDPOINTS --
"""
Since all the requests are performed on the same url, one endpoint would be enough:
@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def ...
    if request.method == 'GET':
        ...

But I prefer (for the sake of the notes) to keep them in separate functions.
"""


# Create record
@app.route('/', methods=['POST'])
def add_entry():
    """
    Add new record to database.
    """
    new_entry = Asimov(request.json['title'], request.json['year'])

    db.session.add(new_entry)
    db.session.commit()

    return jsonify(new_entry.to_dictionary())


# Read records
@app.route('/', methods=['GET'])
def read_entry():
    """
    Displays records found in the database.
    """
    if 'id' in request.args:
        # Display one record found in the db, id matching field
        entry = Asimov.query.get(request.args['id'])

        return jsonify(entry.to_dictionary())

    else:
        # Display all
        all_entries = Asimov.query.all()

        for i in all_entries:
            i.to_dictionary()

        # Populating data
        data = {'books': []}
        for book in all_entries:
            data['books'].append(book.to_dictionary())

        return jsonify(data)


# Update record by id
@app.route('/', methods=['PUT'])
def update_entry():
    """
    Updates one record found in the database.
    @id: matching field to update record.
    """
    entry = Asimov.query.get(request.json['id'])

    # Updating data
    entry.title = request.json['title']
    entry.year = request.json['year']

    db.session.commit()

    return jsonify(entry.to_dictionary())


# Delete record by id
@app.route('/', methods=['DELETE'])
def delete_entry():
    """
    Deletes one record found in the database.
    @id: matching field to delete record.
    """
    entry = Asimov.query.get(request.args['id'])

    db.session.delete(entry)
    db.session.commit()

    return jsonify(entry.to_dictionary())


if __name__ == '__main__':
    app.run(debug=True, port=5002)
