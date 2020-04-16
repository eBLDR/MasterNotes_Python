"""
ODM - Object Document Mapper
Roughly equivalent to SQL ORM.
"""
import pymodm

fields = pymodm.fields

mongo_uri = 'mongodb://localhost:27017/myDatabase'

# Add credentials
# mongo_uri = 'mongodb://username:password@localhost:27017/myDatabase'

# Connect to MongoDB, @alias can be optionally to the connection
pymodm.connection.connect(mongo_uri, alias='my-app')


# Model representing documents in the User collection
class User(pymodm.MongoModel):
    """
    Typically, the definition of a MongoModel class will include one or more
    fields and optionally some metadata, encapsulated in an inner class
    called Meta.

    Field types:
    CharField, IntegerField, FloatField, BooleanField, ListField,
    DictField, DateTimeField ...and many more.

    Fields general keyword parameters:
        @required=is required
        @default=default value
        @choices=array with valid values
        @primary_key=specify different field name
        @blank=if true, allow to be have an empty value

    Each field can specify further parameters.
    """
    first_name = fields.CharField()
    last_name = fields.CharField(required=True)
    email = fields.EmailField()
    alive = fields.BooleanField(default=True)

    # Optional Meta class for manual config
    class Meta:
        # Specify which connection the model will use
        connection_alias = 'my-app'

        # Name of the collection to use. By default, this is the same name as
        # the model, converted to snake case.
        collection_name = 'user'

        # Whether to restrict inheritance on this model. If True, the _cls
        # field will not be stored in the document. False by default.
        final = True


# Saving a single instance of data
first_user = User(
    last_name='Sponge', first_name='NotBob', email='bob@spon.ge'
).save()

print(type(first_user))
print(first_user.last_name, first_user._id)  # _id key created automatically

# Saving instances in bulk - it does not save default values!
users = [
    User('user@email.com', 'Bob', 'Ross'),
    User(email='anotheruser@email.com', first_name='David', last_name='Attenborough')
]
User.objects.bulk_create(users)

# To update, simply change the instance and call save()
first_user.alive = False
first_user.save()

print('=' * 10)

# Accessing data - using `objects` QuerySet attribute
print(type(User.objects))
print(f'Total users: {User.objects.count()}')

print(f'First user is: {User.objects.first().email}')

print('=' * 10)

for user in User.objects.all():
    print(user.first_name, user.email, user.alive)

# Querying with filters - raw accepts all kind of MongoDB's raw query
print('\nM.I.A.:')
for user in User.objects.raw({'alive': False}):
    print(user.first_name)

# Delete a document
first_user.delete()

