import pygal

pieChart = pygal.Pie()
pieChart.title = 'Favourite Pets'

with open('pets.txt', 'r') as file:
    for line in file.read().splitlines():
        if line:  # to avoid error in case there is a empty line at the end of the file .txt
            label, value = line.split(';')  # using the desired character to split the line
            pieChart.add(label, int(value))

pieChart.render_to_file('petsChart.svg')
