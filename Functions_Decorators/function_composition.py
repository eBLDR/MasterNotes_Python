def inner():
    print("I am function inner()!")


def outer(func):
    # Passed-in function is referred to as `callback`
    func()


# Function composition
outer(inner)

print("=" * 30)


def outer2():
    def inner2():
        print("I am function inner2()!")

    return inner2


func2 = outer2()
print(func2)
func2()
outer2()()
