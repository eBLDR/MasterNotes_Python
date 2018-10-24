from sqlalchemy import create_engine
# Session object
from sqlalchemy.orm import sessionmaker
# Table sctructures
from declarative import Address, Base, Person
 
engine = create_engine('sqlite:///example.db', echo=True)

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

print('=' * 30)

# Equivalence to SQL INSERT clause
new_person = Person(name='new person')  # Using the table created in declarative.py
# Inserting a record using the table structure - add()
session.add(new_person)
# commit() will save the transaction - it will call flush(), which send SQL statements to db
session.commit()
 
# Insert an Address in the address table
new_address = Address(post_code='00000', person=new_person)
session.add(new_address)
session.commit()

# If we want to add a collection of objects, use session.add_all(@seq) function

# Roll back also possible
# session.rollback()

print('=' * 30)

# Equivalence to SQL SELECT clause
# all() will fetch all records
all_data = session.query(Person).all()
print(all_data)  # Returns a list with all the records, a list of Person type

# first() ill return the first record
person = session.query(Person).first()
print(person)
print(person.id, person.name)  # Field can be accessed by name

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

# one(), if only one record is expected - if more than one record is found, it will raise an error
address = session.query(Address).filter(Address.person == person).one()
print(address.to_dictionary())

# When using filters, many expressions can be combined usng or_ and_ SQLAlchemy keywords
from sqlalchemy import or_
address = session.query(Address).filter(or_(Address.person == person, Address.post_code == '00000')).first()
print(address.post_code)

print('=' * 30)

# Equivalence to SQL DELETE clause - will delete all the matching records
session.query(Person).filter(Person.name == 'new person').delete()
# session.commit()

