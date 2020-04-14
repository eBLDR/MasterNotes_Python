import mongoengine as me


# Referencing other documents
class Author(me.Document):
    name = me.StringField()


class Book(me.Document):
    title = me.StringField(required=True)

    # Establishing the reference - @class_name
    author = me.ReferenceField(Author)

    # One to many relationship
    # authors = me.ListField(me.ReferenceField(Author))

    # The ReferenceField object takes a keyword reverse_delete_rule for
    # handling deletion rules if the reference is deleted.
    # author = me.ReferenceField(Author, reverse_delete_rule=me.CASCADE)


katzenbach = Author(name='Ucucmber').save()

# ReferenceField that the document object
Book(title='Guide for MongoEngine', author=katzenbach).save()

doc = Book.objects.first()
if doc:
    print(doc, type(doc))
    print(doc.author.name)

print('=' * 20)


# Adding methods to the subclassed document
class Book(me.Document):
    title = me.StringField()
    published = me.BooleanField()

    # queryset_manager return all documents of the collection
    @me.queryset_manager
    def live_posts(clazz, queryset):
        # Filtering by condition
        return queryset.filter(published=True)
