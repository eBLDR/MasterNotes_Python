from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str

    # Optional: it's either the specified type or `None`
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

    # Static values
    alive = True


external_data = {
    'id': '123',
    'name': 'John Doe',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],  # Types are converted if possible
}

user = User(**external_data)
print(user.id)

print(repr(user.signup_ts))

print(user.friends)

print(user.dict())