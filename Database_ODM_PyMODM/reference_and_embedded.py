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
    # Storing the _id of the document we want to reference. To reference
    # multiple documents, we can store these ids in a list.
    # @on_delete: Specify what happens when the referenced object is deleted.
    author = fields.ReferenceField(Author, on_delete=fields.ReferenceField.CASCADE)

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


grim = Author(name='Grim').save()

# Using a document as reference
wald = Post(title='Wald', author=grim).save()

grom = Author(name='Grom').save()
grom_comment = Comment(author=grom, content='WWWAaaAaAaRGH!')

# Embedding a document
wald.comments = [grom_comment]
wald.save()  # Update

# Query
for post in Post.objects.all():
    print(post.title, '-', post.revised_on)
    print(post.author.name)  # Accessing reference
    print(post.comments)  # Accessing embedded

print('#' * 10)

# Custom Query
for post in Post.live_posts():
    print(post.title, '-', post.revised_on, post.published)
    print(post.author.name)
