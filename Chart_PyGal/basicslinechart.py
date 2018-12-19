import pygal


def expression_alpha(x):
    if x % 2 == 0:
        return x ** 2
    else:
        return -(x ** 2)


line_chart = pygal.Line()
line_chart.title = 'Plotting dots'

# creating the x values
X = range(15)
line_chart.x_labels = map(str, X)

# creating the f(x) = y values
Y = []
for i in X:
    Y.append(expression_alpha(i))

line_chart.add('Expression Alpha', Y)

line_chart.render_to_file('line_chart_example.svg')
