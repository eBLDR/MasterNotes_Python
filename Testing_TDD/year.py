class Year:
    def __init__(self, year):
        self.year = year

    def is_leap(self):
        if self.year % 100 == 0 and self.year % 400 != 0:
            return False

        return self.year % 4 == 0
