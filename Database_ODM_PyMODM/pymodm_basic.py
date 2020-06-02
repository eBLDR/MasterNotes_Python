"""
ODM - Object Document Mapper
Roughly equivalent to SQL ORM.
Developed by MongoDB team.
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
    lucky_numbers = fields.ListField()
    stats = fields.DictField()

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
    last_name='Sponge', first_name='NotBob', email='bob@spon.ge',
    stats={
        'weight': 36,
        'height': 124,
    }
).save()

print(type(first_user))
print(first_user.last_name, first_user._id)  # _id key created automatically

print('=' * 10)

# Converting to dict
print(first_user.to_son().to_dict())

print('=' * 10)

# Saving instances in bulk - it does not save default values!
users = [
    User('user@email.com', 'Bob', 'Ross', lucky_numbers=[5, 8, 12]),
    User(email='anotheruser@email.com', first_name='David', last_name='Attenborough')
]
User.objects.bulk_create(users)

# To update, simply change the instance and call save()
first_user.alive = False
first_user.save()

"""
Or use update() method
data = {
    'field_1': 'new_value',
    'field_4': 'new_value',
}

model.objects.raw(
    {'uuid': uuid},  # Filter to query
).update(
    {"$set": data},  # To set the new data
)
"""

print('=' * 10)

# Accessing data - using `objects` QuerySet attribute
print(type(User.objects))
print(f'Total users: {User.objects.count()}')

print(f'First user is: {User.objects.first().email}')

print('=' * 10)

all_users = User.objects.all()
print(type(all_users))

for user in all_users:
    print(user.first_name, user.email, user.alive)

print('=' * 10)

# Querying with filters - raw accepts all kind of MongoDB's raw query
alive_users = User.objects.raw({'alive': False})
print(type(alive_users))

print('=' * 10)

# Querying by items in array
for user in User.objects.raw({'lucky_numbers': 12}):
    print(user.email, user.lucky_numbers)

print('=' * 10)

# Querying by nested fields - accessed by dot notation
# for user in User.objects.raw({'stats.weight': 36}):
# Or using mongo raw query code
for user in User.objects.raw({'stats.height': {'$lt': 150}}):
    print(user.email, user.stats)

print('=' * 10)

# Methods all(), first(), count(), etc can be applied to any type of QuerySet
print(type(alive_users.first()))

print('=' * 10)

print('M.I.A.:')
for user in alive_users:
    print(user.first_name)

# Delete a document
first_user.delete()
