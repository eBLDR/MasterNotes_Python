# Screen input/output

# print(*args, sep=' ', end='\n', file=sys.stdout, flush=False)
# Pipe used is stdout (standard output)
# All non-keyword arguments are converted to strings like str() does and
# written to the stream, separated by sep and followed by end
print(10, 12, 'hello', sep=' & ', end='\n###\n')

# input(prompt='')
# Pipe used is stdin (standard input)
# If the prompt argument is present, it is written to standard output without
# a trailing newline.
# Upon pressing enter key, input() then reads a line from stdin as string
# (stripping a trailing newline), and returns that.
x = input('Character --> ')
print(x)
