class Car:
    def __init__(self, color='red'):
        # Attributes go here
        self.color = color
        self.engine_on = False

        self.fuel = 0
        self.max_fuel = 100

        self.fuel_liters_per_km = 1

        self.total_km = 0

    def display_stats(self):
        print('Engine on: {0}\nFuel: {1:.2}/{2:.2}\nKm: {3:.1}'.format(
            self.engine_on, self.fuel, self.max_fuel, self.total_km
        ))

    def start_engine(self):
        self.engine_on = True
        print('Engine started!')

    def stop_engine(self):
        self.engine_on = False
        print('Engine stopped.')

    def add_fuel(self, liters):
        if self.engine_on:
            print('BOOM!!!')
            exit()

        self.fuel += liters

        if self.fuel > self.max_fuel:
            self.fuel = self.max_fuel
            print('Full tank! Liters: {0:.2}.'.format(self.max_fuel))

        else:
            print('Added {0:.2} liters of fuel.'.format(liters))

    def run(self, km):
        if not self.engine_on:
            print('Engine is not started!')
            return

        if self.fuel < 1:
            print('No petrol!')
            return

        max_km = self.fuel / self.fuel_liters_per_km

        if km <= max_km:
            self.total_km += km
            self.fuel -= km * self.fuel_liters_per_km

        else:
            self.total_km += max_km
            self.fuel = 0
            km = max_km
            print('Not enough fuel...!')

        print('Moved forward {0:.1}km! Total distance is: {1:.1}km'.format(
            km, self.total_km
        ))

    def paint(self):
        pass


class Manager:
    def __init__(self):
        self.car = Car()
        self.valid_options = ['help', 'quit', 'start', 'stop', 'fuel', 'run']

    def run(self):

        while True:
            self.car.display_stats()
            print('=' * 20)

            while True:
                action = input('Action: ').lower()
                if action in self.valid_options:
                    break

            if action == 'quit':
                break

            elif action == 'help':
                print(self.valid_options)

            elif action == 'start':
                self.car.start_engine()

            elif action == 'stop':
                self.car.stop_engine()

            elif action == 'fuel':
                while True:
                    amount = input('Liters (L): ')
                    if amount.isdigit():
                        amount = int(amount)
                        break

                self.car.add_fuel(amount)

            elif action == 'run':
                while True:
                    distance = input('Distance (km): ')
                    if distance.isdigit():
                        distance = int(distance)
                        break
                self.car.run(distance)


if __name__ == '__main__':
    Manager().run()
