import pygal

pie_chart = pygal.Pie()
pie_chart.title = 'Favourite Pets'

with open('pets.csv', 'r') as file:
    for line in file.read().splitlines():
        # To avoid error in case there is a empty line at the end of the file
        if not line:
            continue

        # Using the desired character to split the line
        title, value = line.split(',')
        pie_chart.add(title, int(value))

# Adding a value to show multi-series pie chart
pie_chart.add(
    'Dog',
    [
        {
            'value': 12,
            'label': 'chihuahua',
        },
        {
            'value': 3,
            'label': 'mastiff',
        },
        {
            'value': 6,
            'label': 'collie',
        },
    ]
)

pie_chart.render_to_file('pets_chart.svg')
