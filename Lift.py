class Lift:

    def __init__(self, floors):
        self.position
        self.floors = floors

    def set_position(self, target):
        self.position = target

    def go_to_floor(self, target):
        length_traveled = abs(self.position - target)
        set_position(target)
        return length_traveled

