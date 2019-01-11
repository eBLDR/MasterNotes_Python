# NESTING FUNCTIONS


def spam1():
    def spam2():
        def spam3():
            z = ' even more spam'
            print('In spam3, locals are {}'.format(locals()))
            return z

        y = ' more spam'
        y += spam3()
        print('In spam2, locals are {}'.format(locals()))
        return y

    x = 'spam'
    x += spam2()
    print('In spam1, locals are {}'.format(locals()))
    return x


print(spam1())

print('=' * 30)

# they are identical, because we are in the global scope
print(locals())
print(globals())

print('=' * 30)


# RETURNING FUNCTIONS

def parent(num):
    def first_child():
        return 'Printing from the first_child() function.'

    def second_child():
        return 'Printing from the second_child() function.'

    try:
        assert num == 10
        return first_child
    except AssertionError:
        return second_child


foo = parent(10)
bar = parent(11)

print(foo)
print(bar)

print(foo())
print(bar())
