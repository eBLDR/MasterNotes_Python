"""
pyperclip module has copy() and paste() functions that can send text to and
receive text from your computer’s clipboard. Sending the output of your
program to the clipboard will make it easy to paste it to an email, word
processor, or some other software.
"""
import pyperclip

input('Copy some text to clipboard . . .')

print(pyperclip.paste())

pyperclip.copy('COPY ME')  # copies text to clipboard
pasted = pyperclip.paste()  # pastes text from clipboard

print(pasted)
