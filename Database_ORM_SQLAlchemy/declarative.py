"""
ORM (Object-relational mapping) programs remove the necessity of
writing tedious and error-prone raw SQL statements.
ORM is a programming technique for converting data between incompatible
type systems in object-oriented programming languages.
"""
# Liking engine
from sqlalchemy import create_engine
# ORM mapper
from sqlalchemy.ext.declarative import declarative_base
# Data types
from sqlalchemy import Column, Integer, String, ForeignKey
# Tool resources
from sqlalchemy.orm import relationship

# Creating the base object
Base = declarative_base()


# Creating the table structure
class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'address'
    
    # Here we define columns for the table address
    # Notice that each column is also a normal Python instance attribute
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)


if __name__ == '__main__':
    # Creating engine and Linking to database
    # SQLAlchemy supports different engines (SQLite3, MySQL...)
    engine = create_engine('sqlite:///example.db', echo=True)
    # echo=True will print the statements being processed

    # Create all tables in the engine, equivalent to "Create Table" in raw SQL
    Base.metadata.create_all(engine)
