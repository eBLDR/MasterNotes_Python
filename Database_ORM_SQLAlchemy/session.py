"""
Session object states:

- Transient: an instance that's not included in a session and has not
    been persisted to the database.
- Pending: an instance that has been added to a session but not persisted to a database yet - add()
- Persistent: an instance that has been persisted to the database - commit()
- Detached: an instance that has been persisted to the database but not included in any sessions - close() after commit()
"""

from sqlalchemy import create_engine
# Session object
from sqlalchemy.orm import sessionmaker
# Table sctructures
from declarative import Address, Base, Person
 
engine = create_engine('sqlite:///example.db', echo=False)

# Bind the data to the engine
# Base.metadata.bind = engine

# Creating a db session class
DBSession = sessionmaker(bind=engine)  # By default @autoflush=True

# Instantiating a session
session = DBSession()

query = "SELECT * FROM Person"

# SQL statements can be executed as string queries
buff = session.execute(query, params=None)

print(type(buff))  # It's a generator

for row in buff:
    print(row.id, row)

print('=' * 30)

# Parameters can be passed using
result = session.execute("SELECT * FROM Person WHERE id=:param", {"param":5})

for row in result:
    print(row.id, row.name)

# Sessions must always be closed when finished
session.close()

print('=' * 30)

# CREATE OBJECTS
from sqlalchemy import inspect # To inspect the object states

session = DBSession()

# Equivalence to SQL INSERT clause
new_person = Person(name='new person')  # Using the table created in declarative.py

ins = inspect(new_person)  # A reference to the object to be inspected
print('Object created.')

# Object state
print('Transient: {0}; Pending: {1}; Persistent: {2}; Detached: {3}'.format(ins.transient, ins.pending, ins.persistent, ins.detached))

# Adding a record using the table structure - add()
session.add(new_person)
print('Object added to session.')

# Object state
print('Transient: {0}; Pending: {1}; Persistent: {2}; Detached: {3}'.format(ins.transient, ins.pending, ins.persistent, ins.detached))

# commit() will save the transaction - it will call flush(), which send SQL statements to db
session.commit()
print('Session committed.')

# Object state
print('Transient: {0}; Pending: {1}; Persistent: {2}; Detached: {3}'.format(ins.transient, ins.pending, ins.persistent, ins.detached))

session.close()
print('Session closed.')

# Object state
print('Transient: {0}; Pending: {1}; Persistent: {2}; Detached: {3}'.format(ins.transient, ins.pending, ins.persistent, ins.detached))

print('=' * 20)

session = DBSession()
 
# Insert an Address in the address table
new_address = Address(post_code='00000', person=new_person)
session.add(new_address)

# Id is not assigned until commited to db
print(new_address.id)

session.commit()

# Id already assigned
print(new_address.id)

# If we want to add a collection of objects, use session.add_all(@seq) function

# Roll back also possible
# session.rollback()

print('=' * 30)

# QUERY OBJECTS

# Equivalence to SQL SELECT clause
# all() will fetch all records
all_data = session.query(Person).all()
print(all_data)  # Returns a list with all the records, a list of Person type

# first() ill return the first record
person = session.query(Person).first()
print(person)
print(person.id, person.name)  # Field can be accessed by name

# UPDATE OBJECTS

# Equivalence to SQL UPDATE clause
person.name = 'New Updated Name'  # Updating the attr
session.commit()

# person is an object from Person class, we can access our custom methods
print(person.to_dictionary())

print('=' * 30)

# Using filters - filter(condition), equivalent to SQL WHERE clause
result = session.query(Address).filter(Address.person == person).all()
for i in result:
    print(i.post_code)

print('=' * 30)

try:
    # one(), if only one record is expected - if more than one record is found, it will raise an error
    address = session.query(Address).filter(Address.person == person).one()
    print(address.to_dictionary())
except:
    print('ERROR: one() - More than one record was found.')

# When using filters, many expressions can be combined usng or_ and_ SQLAlchemy keywords
from sqlalchemy import or_
address = session.query(Address).filter(or_(Address.person == person, Address.post_code == '00000')).first()
print(address.post_code)

print('=' * 30)

# DELETE OBJECTS

# Equivalence to SQL DELETE clause - will delete all the matching records
session.query(Person).filter(Person.name == 'new person').delete()

# Will the delelte the @sqlalchemy_object
session.delete(address)

# session.commit()
session.close()

"""
Normal Session - sessiomaker() vs. Scoped Session - scoped_session()

If we open 2 sessions using sessionmaker(), then it won't be possible to add the same
object to both sessions at the same time - an object can only be attached at most one unique session object.

If the session objects are retrieved from a scoped_session object, however,
then we don't have such an issue since the scoped_session object maintains a
registry for the same session object.
"""
