def spam1():
    # Nested functions
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
