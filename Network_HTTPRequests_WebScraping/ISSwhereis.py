""" Retrieving location from ISS and displaying it """

import requests
import turtle
import time

source_url = 'http://api.open-notify.org/iss-now.json'


def get_data(url):
    response = requests.get(url).json()
    # storing data in a more comfortable way
    time_now = response['timestamp']  # UNIX time in seconds
    location = response['iss_position']
    lat = float(location['latitude'])
    lon = float(location['longitude'])
    # print(response)
    # print(response.keys())
    return time_now, lat, lon


def display_prompt():
    # display prompt in the console
    time_now, lat, lon = get_data(source_url)
    print("\nISS position at {} (UNIX seconds from epoch)".format(time_now))
    print("{}".format(time.ctime(time_now)))  # to display time in a more readable way
    print("Latitude: {}\nLongitude: {}".format(lat, lon))


def display_map():
    # display in map
    while True:
        iss.clear()  # to clear the previous printing
        time_now, lat, lon = get_data(source_url)
        iss.goto(lon, lat)
        iss.stamp()

        # printing time in a nice way
        if lon < 0:
            iss.goto(lon + 4, lat + 4)
            iss.write(time.ctime(time_now), align='left', font=14)
        else:
            iss.goto(lon - 4, lat + 4)
            iss.write(time.ctime(time_now), align='right', font=14)

        # refreshing every 5 seconds
        time.sleep(5)


screen = turtle.Screen()
screen.title('ISS - Location in Real Time')
screen.setup(720, 360)
# adjusting coordinates (x lower left, y lower left, x upper right, y upper right)
screen.setworldcoordinates(-180, -90, 180, 90)
# map.jpg is centered at 0,0 real world coordinates
# map.jpg had to be converted to map2.png using Image from PIL, turtle cannot load jpg
screen.bgpic('map2.png')

iss = turtle.Turtle()
iss.hideturtle()
iss.shape('circle')
iss.color('red')
iss.turtlesize(0.4)
iss.penup()

display_prompt()
display_map()

turtle.done()

# TODO fix the terminating of the program
