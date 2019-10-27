"""
COMPOSITION is the technique of assigning a class to a data attribute of another class.
So, an object can be made out of different classes (and also attributes of its own).
i.e.: the Duck object has Wing object, Peak object, Leg object, and so on.
In simple words, composition works when something HAS something, rather than
something IS something (which would be inheritance).

AGGREGATION, unlike composition, aggregation uses existing instances of objects to build up another object.
The composed object doesn't actually own the objects that it's composed of, if it's destroyed,
those objects continue to exist.
"""
import random


class Engine:
    def __init__(self):
        self.on = False

    def is_on(self):
        return self.on

    def start(self):
        self.on = True

    def stop(self):
        self.on = False


class Wheel:
    def __init__(self):
        self.is_flat = False
        self.chance_of_flat = 0.05

    def spin(self):
        if random.random() < self.chance_of_flat:
            self.is_flat = True
            return True


class Bike:
    def __init__(self):
        self.number_of_wheels = 2
        self.km = 0

        # Composition
        self.engine = Engine()

        # Composition - using a container
        self.wheels = [Wheel() for _ in range(self.number_of_wheels)]

    def display(self):
        print('Engine: {}'.format(
            'on' if self.engine.is_on() else 'off'
        ))

        for wheel in self.wheels:
            print('Wheel is: {}'.format(
                'flat' if wheel.is_flat else 'OK'
            ))

    def start(self):
        # Delegation
        self.engine.start()

    def stop(self):
        # Delegation
        self.engine.stop()

    def check_wheels(self):
        return not any([wheel.is_flat for wheel in self.wheels])

    def run(self):
        # Using the object of composition
        if not self.engine.is_on():
            print('Engine is off!')
            return

        if not self.check_wheels():
            print('Some of the wheels are flat...')
            return

        self.km += random.randint(50, 100)

        # Using the container of composed objects
        for wheel in self.wheels:
            if wheel.spin():
                # Got a flat tyre
                print('We got a flat tyre...!')

        print('We moved a total of {}km.'.format(self.km))


class Manager:
    def __init__(self):
        # Composition
        self.bike = Bike()

        self.actions = {
            'start': self.bike.start,
            'stop': self.bike.stop,
            'run': self.bike.run,
            'exit': self._exit
        }

    def main(self):
        while True:
            self.bike.display()

            action = self.get_action()

            # Run action
            action()

    @staticmethod
    def _exit():
        exit()

    def get_action(self):
        while True:
            option = input('Option: ').lower()
            if option in self.actions.keys():
                return self.actions[option]


if __name__ == '__main__':
    Manager().main()
