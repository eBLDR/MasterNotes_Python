while True:
    try:
        text = input('Enter something --> ')

    # Triggered by Ctrl+D
    except EOFError:
        print('Why did you do an EOF on me?')

    # Triggered by Ctrl+C
    except KeyboardInterrupt:
        print('You cancelled the operation... or no.')

    else:
        print('You entered {}'.format(text))

        if 'exit' in text.lower() and 'please' in text.lower():
            break
