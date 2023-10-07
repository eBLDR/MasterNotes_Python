"""
MongoDB is a NoSQL database that works on a server.
It stores data (documents) in JSON like format.
Before running this python script, Mongo server must be running.
"""
import datetime
import pprint

from pymongo import MongoClient

# Establishing connection
client = MongoClient()

# If not specified, these are the default values for host and port
# client = MongoClient('localhost', 27017)

# Equivalent URI
# client = MongoClient('mongodb://localhost:27017')

# Get a list of the names of all databases on the connected server
print(f'Databases are: {client.list_database_names()}')

# Accessing a database - creates new database implicitly upon first use
db = client.my_mongo_db

print('Connected to:', db)
print(type(db))

# Equivalent dictionary-style access, or client.get_database(<db_name>)
db2 = client['my_mongo_db']
print(db2)
print(db == db2)

# Drop database
# client.drop_database(db_name)

# Display existing collections
print(f'Existing collections are: {db.list_collection_names()}')

print('=' * 20)

# Creating new/accessing a collection
collection = db.collection
print(type(collection))

# Equivalent dictionary-style access, or db.get_collection(<collection_name>)
collection2 = db['collection2']
print(collection2)
print(collection == collection2)

# Drop a collection
db.collection2.drop()

print('=' * 20)

"""
Note on the lazy creation of MongoDB:
Collections and databases are created when the first document is inserted into
them. So, none of the above commands have actually performed any operations
on the MongoDB server.
"""

# Inserting documents
# _id field can be manually specified, otherwise it will take a random
# ObjectId value.
# Many kinds of native python data are allowed
document_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Rambo',
    'year': 2036,
    'date': datetime.datetime.utcnow(),
    'tags': ['wow', 'gotcha', 'epic'],
}

# Insert 1 document
result = collection.insert_one(document_1)
print(f'One post: {result.inserted_id}')

# Insert many documents - an array
document_2 = {
    'title': 'Virtual Environments',
    'author': 'Rambo',
    'year': 2000,
}

document_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill',
    'year': 1,
}

new_result = collection.insert_many([document_2, document_3])
print(f'Multiple posts: {new_result.inserted_ids}')

print('=' * 20)

# Retrieving documents - returns the first document
print(collection.find_one())

# Using a dictionary with field to match as an argument
print(collection.find_one({'author': 'Bill'}))

# Retrieves all matching documents - filter is optional
# collection.find() will return all documents in an iterable cursor object
# cursor modifier .limit(<n>) can be used to set a limit of fetched documents
scott_posts = collection.find({'author': 'Rambo'})  # .limit(5)
print(scott_posts)
print(type(scott_posts))

# To find by ObjectId
from bson import ObjectId

print(collection.find({'_id': ObjectId(result.inserted_id)}))

# Using MongoDB filters
print(collection.find({'year': {'$gt': 1900}}))

# It's a cursor object - iterable
for post in scott_posts:
    print(post)

print('=' * 20)

# Counting documents
print(collection.count_documents({'year': 1}))

# Sort results
for document in collection.find().sort('year'):
    pprint.pprint(document)

# Update
collection.update_one(
    {'_id': ObjectId(result.inserted_id)},
    {'$set': {'year': 3000}},
)

# Delete
# collection.delete_many(filters)

# Aggregation pipeline
pipeline = [
    {}
]

results = collection.aggregate(pipeline)

for result in results:
    print(result)
