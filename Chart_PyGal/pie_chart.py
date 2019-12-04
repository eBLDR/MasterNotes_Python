import pygal

pie_chart = pygal.Pie()
pie_chart.title = 'Favourite Pets'

with open('pets.txt', 'r') as file:
    for line in file.read().splitlines():
        # to avoid error in case there is a empty line at the end of the
        # file .txt
        if line:
            # using the desired character to split the line
            label, value = line.split(';')
            pie_chart.add(label, int(value))

pie_chart.render_to_file('pets_chart.svg')
