"""
ORM (Object-relational mapping) programs remove the necessity of
writing tedious and error-prone raw SQL statements.
ORM is a programming technique for converting data between incompatible
type systems in object-oriented programming languages.
"""
# Linking engine
from sqlalchemy import create_engine
# ORM mapper
from sqlalchemy.ext.declarative import declarative_base
# Data types
from sqlalchemy import Column, Integer, String, ForeignKey
# Tool resources
from sqlalchemy.orm import relationship

# Creating the base object
Base = declarative_base()


# A custom declarative base can be declared, if we wish to
class CustomBase(Base):
    __abstract__ = True
    
    def to_dictionary(self):
        # This method populates a dictionary with the attributes : values
        tmp = {}
        for i in self.__table__.columns:
            tmp[i.name] = getattr(self, i.name)
        return tmp
    

# Creating the table structure
class Person(CustomBase):
    __tablename__ = 'person'  # Name of the table in database

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(CustomBase):
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
    # Creating engine and linking to database
    # SQLAlchemy supports different engines (SQLite3, MySQL...)
    engine = create_engine('sqlite:///example.db', echo=True)
    # echo=True will print the statements being processed

    # Create all tables in the engine, equivalent to "Create Table" in raw SQL
    Base.metadata.create_all(engine)
