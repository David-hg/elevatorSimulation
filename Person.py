class Person:

    def __init__(self, steps_without_change, floor, door):
        self.in_home = True
        self.ready_to_use_lift = True
        self.waiting_steps = steps_without_change
        self.actual_waiting_steps = 0
        self.home = (floor, door)

    def update_actual_waiting_steps(self):
        if self.actual_waiting_steps - 1 == 0:
            self.actual_waiting_steps = 0
            self.ready_to_use_lift = True
            return True
        else:
            self.actual_waiting_steps = max(0, self.actual_waiting_steps - 1)
            return False
