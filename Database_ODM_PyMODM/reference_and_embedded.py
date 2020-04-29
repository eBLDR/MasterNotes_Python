import datetime

import pymodm

fields = pymodm.fields

pymodm.connection.connect('mongodb://localhost:27017/myDatabase')


class Author(pymodm.MongoModel):
    name = fields.CharField(required=True)


class Comment(pymodm.MongoModel):
    author = fields.ReferenceField(Author)
    content = fields.CharField(required=True)


class Post(pymodm.MongoModel):
    title = fields.CharField()
    published = fields.BooleanField(default=True)

    # Referencing another document from another collection.
    # Storing the _id of the document we want to reference.
    # @on_delete: Specify what happens when the referenced object is deleted.
    author = fields.ReferenceField(Author, on_delete=fields.ReferenceField.CASCADE)

    # Referencing multiple documents is done by using a list of references.
    authors = fields.ListField(fields.ReferenceField(Author, on_delete=fields.ReferenceField.PULL))

    revised_on = fields.DateTimeField(default=datetime.datetime.utcnow)
    content = fields.CharField()

    # If we don’t need to query the referenced documents outside of our
    # reference structure, we might just embed such documents directly inside
    # the documents that reference them. Either a single one or in a list.
    # Embedded models WON'T be stored in a new collections, rather as a
    # property inside the collection where it is embedded.
    comments = fields.EmbeddedDocumentListField(Comment)

    # Custom query
    @classmethod
    def live_posts(cls):
        return cls.objects.raw({'published': True})

    # Querying by reference field's id
    @classmethod
    def get_by_author(cls, author_):
        return cls.objects.raw({'author': author_._id})

    # Querying by reference field's other attributes
    @classmethod
    def get_by_author_name(cls, author_name):
        return cls.objects.raw({'author': {'name': author_name}})


grim = Author(name='Grim').save()
grom = Author(name='Grom').save()

# Using a document as reference
wald = Post(title='Wald', author=grim).save()

# Multiple reference
wald_2 = Post(title='Wald 2', authors=[grim, grom]).save()

# Embedding a document
grom_comment = Comment(author=grom, content='WWWAaaAaAaRGH!')

wald.comments = [grom_comment]
wald.save()  # Update


# Query
for post in Post.objects.all():
    print(post.title, '-', post.revised_on)

    # Accessing individual reference
    if post.author:
        print('Single author:')
        print(post.author.name)

    # Accessing multiple reference
    if post.authors:
        print('Multiple authors:')
        for author in post.authors:
            print(author.name)

    # Accessing embedded
    print('Comments:')
    print(post.comments)

    print('=' * 10)

print('#' * 10)

# Custom Query
for post in Post.live_posts():
    print(post.title, '-', post.revised_on, post.published, post.author, post.authors)

print('#' * 10)

# Query  by reference field's id
for post in Post.get_by_author(grim):
    print(post.title, post.author, post.authors)

print('#' * 10)

# Query  by reference field other attributes
for post in Post.get_by_author_name(grim.name):
    print(post.title, post.author, post.authors)

