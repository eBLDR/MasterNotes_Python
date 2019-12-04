# Custom module/package import
import importlib

# Don't type the module extension!
mod_available = ['local', 'production']

while True:
    mod_to_be_imported = input('{}: '.format(mod_available))
    if mod_to_be_imported in mod_available:
        break

# import_module(@mod_name, @package=None) returns the module object
# If package isn't specified, it will take the working directory
module = importlib.import_module(mod_to_be_imported)
print(type(module))

print(dir(module))
print('Name:', module.__name__, '; Pkg:', module.__package__)
print(module.url)
