"""
Deferred import consist on importing the necessary module only within
the scope where it is used.
That is used as workaround to circular imports, for instance.
"""
import random


def init_script():
    # Deferred import
    import sys
    print(sys.modules)


print(random.random())
init_script()
