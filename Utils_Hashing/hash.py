"""
hashlib can perform MD5 (RSA type), SHA1, SHA224, SHA256, SHA384 and SHA512 hash algorithms.
Hashes usually contain only hexadecimal digits.
"""
import hashlib

# Must be encoded as a byte string
password = b'mysecurepassword'
print(password)

# Will return a md5 hash object
hashed_md5 = hashlib.md5(password)
print(hashed_md5)

# Will digest the object
digested_hash = hashed_md5.hexdigest()
print('md5 hashed:', digested_hash)  # It's type str

print('sha1 hashed:', hashlib.sha1(password).hexdigest())

# Adding multiple strings
m = hashlib.md5()  # Creating the object
m.update(b'Nobody inspects me')  # Adding byte string to it
m.update(b'never ever')

m_hashed = m.hexdigest()
print(m_hashed)
print(len(m_hashed))  # Always 32 chars
