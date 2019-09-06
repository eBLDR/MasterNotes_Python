# Access to underlying platform’s identifying data.

import platform

# Queries the given executable for various architecture information.
# @executable=sys.executable - defaults to the Python interpreter binary
print('Architecture,', platform.architecture())

# Returns the machine type, e.g. 'i386'.
print('Machine,', platform.machine())

# Returns the computer’s network name (may not be fully qualified!).
print('Node,', platform.node())

# Returns a single string identifying the underlying platform with as much useful information as possible.
print('Platform,', platform.platform())

# Returns the (real) processor name, e.g. 'amdk6'.
print('Processor,', platform.processor())

# Returns the system’s release, e.g. '2.2.0' or 'NT'
print('Release,', platform.release())

# Returns the system/OS name, e.g. 'Linux', 'Windows', or 'Java'.
print('System,', platform.system())

# Returns (system, release, version) aliased to common marketing names used for some systems. It also does some reordering of the information in some cases where it would otherwise cause confusion.
# print('System alias,', platform.system_alias(system, release, version))

# Returns the system’s release version, e.g. '#3 on degas'.
print('Version,', platform.version())

# Fairly portable uname interface. Returns a namedtuple() containing six attributes: system, node, release, version, machine, and processor.
print('Uname,', platform.uname())

# Python related info
# Returns the Python version as string 'major.minor.patchlevel'.
print('Python version,', platform.python_version())

# Returns the Python version as tuple (major, minor, patchlevel) of strings.
print('Python version tuple,', platform.python_version_tuple())

# Returns a string identifying the Python implementation. Possible return values are: ‘CPython’, ‘IronPython’, ‘Jython’, ‘PyPy’.
print('Python implementation,', platform.python_implementation())

# Returns a tuple (buildno, builddate) stating the Python build number and date as strings.
print('Python build,', platform.python_build())

# Returns a string identifying the compiler used for compiling Python.
print('Python compiler,', platform.python_compiler())

# Returns a string identifying the Python implementation SCM branch.
print('Python SCM branch,', platform.python_branch())

# Returns a string identifying the Python implementation SCM revision.
print('Python SCM revision,', platform.python_revision())
