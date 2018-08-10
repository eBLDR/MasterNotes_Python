"""
The scope of a variable is where it can be seen or used.
LOCAL (local namespace) scope variables are the ones declared inside the function, they cannot be seen from outside
of the function.

GLOBAL (global namespace) scope variables are the ones declared in the main body, outside all functions, they can be
seen (and used as a comparision) from anywhere, and modified only if the object is mutable,
if trying to change a immutable object, Python will create a new local variable instead.
Shadowing a variable means the we are using the same name for a local variable and for a global variable simultaneously,
it's a bad idea.

OUTER scope refers to looking variables declared in the global namespace. ENCLOSING scope refers to the NONLOCAL ones.
A function should be self-contained, should not make changes to global variables, ideally. If it's necessary, just
type 'global variableName' in the first line of the function when defining it. When a function changes the value of
a global variable (or appends/removes items from a list), it's called side effect

--- LEGB Scope Rule, order of namespaces used when searching for variable names ---

L, Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.
E, Enclosing-function locals — Names in the local scope of any and all statically enclosing functions (def or lambda),
from inner to outer.
G, Global (module) — Names assigned at the top-level of a module file, or by executing a global statement in a def
within the file.
B, Built-in (Python) — Names preassigned in the built-in names module : open,range,SyntaxError,...
"""
def add_to_local(number):
    # number is a local variable
    number += 1
    print('I am inside add_to_local(), number is:', number)


number = 0
print('number is:', number)
print('Calling add_to_local()...')
add_to_local(number)
print('number is:', number)

print('=' * 20)


def add_to_global():
    # global is a declaration which holds for the entire current code block,
    # it means that the listed identifiers are to be interpreted as globals
    global number
    number += 1
    print('I am inside add_to_local(), adding 1 to number.')


print('number is:', number)
print('Calling add_to_gloal()...')
add_to_global()
print('number is:', number)

print('=' * 20)


def add_to_nonlocal():
    index = 0
    print('I am inside add_to_nonlocal(), index is:', index)
    def adding():
        # nonlocal causes the listed identifiers to refer to previously bound variables
        # in the nearest enclosing scope excluding globals
        nonlocal index
        index += 1
        print('I am inside adding() nested inside add_to_nonlocal(), index is:', index)

    adding()
    
    print('I am inside add_to_nonlocal(), index is:', index)


add_to_nonlocal()
