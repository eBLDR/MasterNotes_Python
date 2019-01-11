"""
ODM - Object Document Mapper
Roughly equivalent to SQL ORM.
"""
import datetime
from mongoengine import *

# Connecting to the running instance of Mongo - redundant default values
connect('mongoengine_test', host='localhost', port=27017)


# Defining a document for data validation
class Post(Document):
    # Document's data
    # @required=is_required, @max_length=number_of_chars,
    # @default=default_value, @choices=array_with_valid_values,
    # @unique=must_be_unique, @db_field=specify_different_field_name
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)


# Saving a document - If the document already exists in the database,
# then all of the changes will be made on the atomic level to the existing
# document. If it does not exist, however, then it will be created.
post_1 = Post(
    title='Sample Post',
    content='Some engaging content',
    author='Scott'
)

# save() will validate the data against the schema declared in the class
# This will perform an insert
post_1.save()
print(post_1.title)

post_1.title = 'A better post title'

# This will perform an atomic edit - update
post_1.save()
print(post_1.title)

# Leaving a required field off
post_2 = Post(content='Content goes here', author='Michael')

try:
    post_2.save()
except ValidationError as exc:
    print(exc)

print('=' * 20)


# Adding methods to the subclassed document
class Book(Document):
    title = StringField()
    published = BooleanField()

    # queryset_manager return all documents of the collection
    @queryset_manager
    def live_posts(clazz, queryset):
        # Filtering by condition
        return queryset.filter(published=True)


# Referencing other documents
class Author(Document):
    name = StringField()


class Book(Document):
    # Establishing the reference - @class_name
    author = ReferenceField(Author)


doc = Book.objects.first()
if doc:
    print(doc.author.name)
