"""
conftest.py declares fixtures and other shared objects across tests. They have
directory scope.
"""
import pytest


# Fixtures and objects are accessed by other tests by name
@pytest.fixture()
def some_stuff():
    return 'some stuff'
