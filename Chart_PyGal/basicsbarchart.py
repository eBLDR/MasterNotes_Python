import pygal

# if we wish to change the style
from pygal.style import NeonStyle

bar_chart = pygal.Bar(style=NeonStyle)  # create new graph object, type bar
# spcifying the style is not necessary, DefaultStyle by default

# add a title
bar_chart.title = 'Remarquable sequences'

# adding labels
bar_chart.x_labels = map(str, range(11))

# add a set of values to the chart ('table name', items)
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

# add another set
bar_chart.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12])


# render to a new file .svg
bar_chart.render_to_file('bar_chart_example.svg')
