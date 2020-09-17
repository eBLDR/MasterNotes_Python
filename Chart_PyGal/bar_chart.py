import pygal

# If we wish to change the style
from pygal.style import NeonStyle

# Config object
from pygal import Config

config = Config()
config.show_legend = True
config.human_readable = True
config.fill = True
config.print_values = True
config.print_labels = True
config.style = NeonStyle  # DefaultStyle by default

# Create new graph object, type bar
bar_chart = pygal.Bar(config=config)

# Add a title
bar_chart.title = 'Remarkable sequences'

# Adding labels
bar_chart.x_labels = map(str, range(11))

# Add a set of values to the chart ('table name', items)
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

# Add another set
bar_chart.add('Padovan', [1, 1, 1, 2, 2, 3, 4, 5, 7, 9,
                          # Value configuration is possible
                          {
                              'value': 12,
                              'label': 'Last Padovan number!',
                              'color': 'Red',  # Forcing color
                          }])

# Render to new SVG
bar_chart.render_to_file('bar_chart_example.svg')

# render to new PNG file
bar_chart.render_to_png('bar_chart_example.png')
