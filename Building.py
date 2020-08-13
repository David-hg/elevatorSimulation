import numpy as np
from Lift import Lift
class Building:

    def __init__(self, floors_list, num_floors, steps_without_change_matrix):
        self.num_floors = num_floors

        self.lifts = []
        if type(floors_list[0]) is list:
            for x in floors_list:
                self.lifts.append(Lift(x))
        else:
            self.ascensores.append(Lift(floors_list))

        self.person_resting_steps = np.zeros((len(steps_without_change_matrix), len(steps_without_change_matrix[0])), dtype=int)
        self.people_minimum_waiting_steps = steps_without_change_matrix
        self.people_in_home = np.ones((len(steps_without_change_matrix), len(steps_without_change_matrix[0])))

    def get_next_step(self):
        probabilities = self.


