import mongoengine as me

me.connect('mongoengine_test')


# Referencing other documents
class Author(me.Document):
    name = me.StringField()


class Magazine(me.Document):
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
Magazine(title='Guide for MongoEngine', author=katzenbach).save()

doc = Magazine.objects.first()
if doc:
    print(doc, type(doc))
    print(doc.author.name)

print('=' * 20)


# Adding methods to the subclassed document
class Book(me.Document):
    title = me.StringField()
    published = me.BooleanField()
    year = me.IntField()

    # queryset_manager search in all documents
    @me.queryset_manager
    def live_books(doc_cls, queryset):
        # Filtering by condition
        return queryset.filter(published=True)

    # It is possible also to override the `objects` method
    @me.queryset_manager
    def objects(doc_cls, queryset):
        # Sort them by default
        return queryset.order_by('-year')


Book(title='Epic I', published=True, year=1998).save()
Book(title='Epic II', published=False, year=2003).save()

for book in Book.live_books():
    print(book.title, book.published)

print('=' * 20)

for book in Book.objects():
    print(book.title, book.year)
