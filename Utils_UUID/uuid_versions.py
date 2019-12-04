"""
UUID (Universally Unique IDentifier) is a 128-bit number used to identify information.
MD5 and SHA-1 are both cryptographic (hash) functions.
"""
import uuid

# Make a UUID based on the host ID (MAC address) and current time
# Partially equal on each execution
u1 = uuid.uuid1()
print(u1)
print(type(u1))

# Make a UUID using an MD5 hash of a namespace UUID and a name
# Totally equal on each execution
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'anystring'))

# Make a random UUID
# Totally different on each execution
print(uuid.uuid4())

# Make a UUID using a SHA-1 hash of a namespace UUID and a name
# Totally equal on each execution
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'anystring'))
# When NAMESPACE_DNS is specified, the string is a fully-qualified domain name
