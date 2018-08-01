# More compact, usually works together with comprehensions

x = 12

# Expression must have at least one if and one else
expr = "Twelve" if x == 12 else "unknown"
print(expr)

# Cannot contain any elif, but can have multiple if/else
menu = [['eggs', 'bacon'], ['eggs', 'bread'], ['bread', 'bacon'], ['bread']]
for ingredients in menu:
    print(ingredients, "Contains meat" if 'bacon' in ingredients else "Contains eggs"
          if 'eggs' in ingredients else "Boring dish")
# The order is important, the first True condition will be the one to be executed
# Notice that the last else clause will always be executed if none of the previous conditions is True

print('=' * 20)

# fizz buzz game
for x in range(1, 31):
    fizzbuzz = "fizz buzz" if x % 15 == 0 else 'fizz' if x % 3 == 0 else 'buzz' if x % 5 == 0 else str(x)
    print(fizzbuzz)
