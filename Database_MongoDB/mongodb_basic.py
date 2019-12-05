"""
MongoDB is a NoSQL database that works on a server.
It stores data (documents) in JSON like format.
Before running the python script, Mongo server must be running.
"""
from pymongo import MongoClient

# Establishing connection
client = MongoClient()

# If not specified, these are the default values for host and port
# client = MongoClient('localhost', 27017)

# Equivalent URI
# client = MongoClient('mongodb://localhost:27017')

# Accessing database - pymongo_test is a mock db
db = client.pymongo_test
print(db)
print(type(db))

# Equivalent dictionary-style access
db2 = client['pymongo_test']
print(db2)

print(db == db2)

print('=' * 20)

# Creating a new collection - equivalent to SQL tables
# collection_name = db.collection_name
posts = db.posts
print(type(posts))

# Inserting documents - equivalent to SQL records
post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}

# Insert 1 document
result = posts.insert_one(post_1)
print('One post: {0}'.format(result.inserted_id))

# Insert many documents - an array
post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'Scott'
}
post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
}

new_result = posts.insert_many([post_2, post_3])
print('Multiple posts: {0}'.format(new_result.inserted_ids))

print('=' * 20)

# Retrieving documents
# Using a dictionary with field to match as an argument
# Retrieves 1 document
bills_post = posts.find_one({'author': 'Bill'})
print(bills_post)

# Retrieves all matching documents
scott_posts = posts.find({'author': 'Scott'})
print(scott_posts)

# It's a cursor object - iterable
for post in scott_posts:
    print(post)
