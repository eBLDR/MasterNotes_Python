import pytest


# pytest allows to use the keyword `assert` directly
def test_always_passes():
    assert True


def test_always_fails():
    assert False


# Defining fixtures
@pytest.fixture
def example_data():
    return [
        {
            "name": "Crud",
            "title": "Senior Software Engineer",
        },
        {
            "name": "Stake",
            "title": "Project Manager",
        },
    ]


# Function to  be tested
def format_data(data):
    """Simulation."""


# The fixture is used by adding it as an argument to the test,
# its value will be the return value of the fixture function
def test_format_data(example_data):
    assert format_data(example_data) == [
        "Crud: Senior Software Engineer",
        "Stake: Project Manager",
    ]


# Accessing data declared in conftest.py
def test_conftest(some_stuff):
    print(some_stuff)
