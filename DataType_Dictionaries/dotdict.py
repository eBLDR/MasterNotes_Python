class DotDict(dict):
    """
    A dictionary class of which it's keys can be accessed in dot notation.
    Example:
    >>> d = DotDict(a=1, b=2, c=3)
    >>> d['a']
    1
    >>> d.a
    1
    >>> d.z = 0
    >>> d.z
    0
    """

    def __init__(self, **kwds):
        self.update(kwds)
        self.__dict__ = self


a = DotDict(x=0, y=1)
print('a[\'x\']:', a['x'])
print('a.x:', a.x)

a.z = -1
print('a.z = 1\na.z:', a.z)

