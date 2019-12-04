"""
Python is an interpreted high-level programming language for general-purpose
programming. It features a dynamic type system and automatic memory management,
and it supports multiple programming paradigms.

- Physical Line: is what you see when you write the program.
- Logical Line: is what python sees as a single statement.

- STATEMENTS: are a logical lines, make use of keywords that Python understands
(return, import, pass...).

- COMPOUND STATEMENTS: are groups of different statements that work together,
made of one or more clauses.

- CLAUSES: consist of a header and a block of code; each header starts with a
keyword and ends with a colon, the code block is on the same indentation level.

- INDENTATION: leading whitespace (spaces and tabs), all statements at the
same indentation level are called a BLOCK. Indentation = 4 whitespaces.
"""

# This is a single-line comment, this line will be ignored.

"""
This is a multi-line comment, all these lines will be ignored.

Code tells you how, comments should tell you why.

Comments are used to:
    - Explain assumptions
    - Explain important decisions
    - Explain important details
"""

# Creating a variable
v = 'Hello World'

# Printing the variable
print(v)

"""
If we want to specify more than one logical line on a single physical line, we
can explicitly specify it by using ";" separator, which indicated the end of
the logical line/statement.

However, python encourages not to use semicolon separator, and sticking to
writing a maximum of a single logical line on each single physical line.
"""

i = 5
print(i)

# It's the same as
i = 5; print(i)

# Explicit line join - if the line is too long we can use the "\" separator
my_long_var_name = \
    5000000000

# Implicit line join - enclosed with parenthesis, brackets, or curly brackets
my_long_var_name_2 = (
    123, 456, 789
)
