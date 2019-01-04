# Screen input/output

# print(*args, sep=' ', end='\n', file=sys.stdout, flush=False) - pipe is stdout (standard output)
# All non-keyword arguments are converted to strings like str() does and written to the stream,
# separated by sep and followed by end
print(10, 12, 'hello', sep=' & ', end='\n###\n')

# input(prompt) - if the prompt argument is present, it is written to standard output without a trailing newline
# the function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that
# Pipe is stdin (standard input)
x = input('Character --> ')
print(x)
