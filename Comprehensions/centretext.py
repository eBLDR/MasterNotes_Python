def centre_text(*args, column=80):
    text = ''
    for arg in args:
        text += str(arg) + '-'  # to be able to see the trailing spaces
    left_margin = (column - len(text)) // 2
    print(" " * left_margin, text)


centre_text("spam and eggs")
centre_text(12)
centre_text('first', 'second', 3, 12, 'spam')


def centre_text_comp(*args, column=80):
    text = '-'.join([str(arg) for arg in args])
    left_margin = (column - len(text)) // 2
    print(" " * left_margin, text)


centre_text_comp("spam and eggs")
centre_text_comp(12)
centre_text_comp('first', 'second', 3, 12, 'spam')
