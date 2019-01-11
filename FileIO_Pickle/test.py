import pickle

# Converting to/from byte-stream

x = 144
x_serial = pickle.dumps(x)  # converts into hex
print(x_serial)

x_recover = pickle.loads(x_serial)  # to recover the original value
print(x_recover)

s = 'bldr'
s_serial = pickle.dumps(s)  # works for str also
print(s_serial)

s_recover = pickle.loads(s_serial)  # to recover the original value
print(s_recover)
