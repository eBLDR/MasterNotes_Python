"""
ODM - Object Document Mapper
Roughly equivalent to SQL ORM.
"""
import datetime

import mongoengine as me

# Connecting to the running instance of MongoDB
# host and port are redundant default values
me.connect('mongoengine_test', host='localhost', port=27017)


# Defining a collection's structure for data validation
class Post(me.Document):
    """
    Field types:
    StringField, IntField, FloatField, BooleanField, ListField,
    DictField, DateTimeField, DateField ...and many more.

    Fields general keyword parameters:
        @required=is_required
        @default=default_value
        @choices=array_with_valid_values
        @unique=must_be_unique
        @db_field=specify_different_field_name

    Each field can specify further parameters.
    """

    # StringField(@max_length=number_of_chars
    title = me.StringField(required=True, max_length=200)
    content = me.StringField()
    author = me.StringField(required=True, max_length=50)

    year = me.IntField(required=True)

    published = me.DateTimeField(default=datetime.datetime.utcnow)

    # Saving an array
    tags = me.ListField(me.StringField())

    # Specify config
    meta = {
        'collection': 'custom_collection_name',  # By default, a collection
        # name with the past name in lowercase is used

        # Capped collection - documents cannot change their size!!
        # 'max_documents': 1000,  # Set the maximum documents in collection
        # 'max_size': 2000000,  # Max disk space (rounded to multiple of 256)

        'allow_inheritance': True,  # To allow inheritance
    }


class ImagePost(Post):
    image_path = me.StringField()


# Saving a document - If the document already exists in the database,
# then all of the changes will be made on the atomic level to the existing
# document. If it does not exist, however, then it will be created.
post_1 = Post(
    title='Sample Post',
    content='Some engaging content',
    author='Mambo',
    year=1999,
    tags=['cool', 'warm'],
)

# save() will validate the data against the schema declared in the class
# and perform an insert
post_1.save()
print(post_1.title)

# Update, simply save()
post_1.title = 'A better post title'

# This will perform an atomic edit - update
post_1.save()
print(post_1.title)

# Leaving a required field off
post_2 = Post(content='Content goes here', author='Mich')

try:
    # Adding @validate=False parameter will skip validation
    post_2.save()
except me.ValidationError as exc:
    print(exc)

print('=' * 20)

# Accessing data
"""
Document classes have an objects attribute, which is used for accessing the
objects in the database associated with the class. The objects attribute is
a QuerySetManager, which creates and returns a new QuerySet object on access.
The QuerySet object may be iterated over to fetch documents from the database.
"""
print(type(Post))
print(Post.objects.first())  # Only first document

# All documents
for post in Post.objects:
    print(post)
    print(post.title)

# Adding filters - calling the QuerySet with field lookup keyword arguments
for post in Post.objects(author='Mambo'):
    print(post.author)

# Query by value in array
for post in Post.objects(tags='cool'):
    print(post.tags)

# Raw queries can be added
for post in Post.objects(__raw__={'year': {'$lt': 2020}}):
    print(post.year)

# Counting
print(Post.objects().count())

# Sorting - add `+` or `-` to specify ascending or descending sorting
print(Post.objects().order_by('-year'))  # , '-author')) It can concatenate orders

# Delete a document
match = Post.objects(author='Mambo').first()
print(f'Deleting {match}, {match.title}')
match.delete()

# Drop entire collection
# Post.drop_collection()
