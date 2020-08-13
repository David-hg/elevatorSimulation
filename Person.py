class Person:

    def __init__(self, floor, steps_without_change):
        self.floor = floor
        self.in_home = True
        self.steps_without_change = steps_without_change

    def change_home_state(self, in_home):
        self.in_home = in_home