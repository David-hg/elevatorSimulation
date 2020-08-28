import numpy as np
from LiftController import LiftController
from Person import Person


class Building:

    def __init__(self, lifts_list, steps_without_change_matrix):
        self.total_distance = 0
        self.persons = []
        self.available_persons = []
        current_floor = current_door = 0
        for steps_without_change_by_floor in steps_without_change_matrix:
            current_floor += 1
            for steps_without_change_by_home in steps_without_change_by_floor:
                current_door += 1
                for steps_without_change_by_person in steps_without_change_by_home:
                    new_person = Person(steps_without_change_by_person, current_floor, current_door)
                    self.persons.append(new_person)
                    self.available_persons.append(new_person)
            current_door = 0
        self.lift_controller = LiftController(lifts_list)

    def get_next_person(self):
        selected_person = np.random.choice(self.available_persons)
        return selected_person

    def run(self, n_steps=100000):
        for i in range(len(n_steps)):
            next_person = self.get_next_person()
            current_floor = 0 if not next_person.in_home else next_person.home[0]
            target_floor = 0 if next_person.in_home else next_person.home[0]
            selected_lift = self.lift_controller.get_closest_lift(current_floor)
            self.total_distance += self.lift_controller.move_lift(selected_lift, current_floor, target_floor)
            if next_person.waiting_steps > 0:
                next_person.actual_waiting_steps = next_person.waiting_steps
                self.available_persons.remove(next_person)
            next_person.in_home = not next_person.in_home
            for person in self.persons:
                ready_to_use_lift = person.update_actual_waiting_steps()
                if ready_to_use_lift:
                    self.available_persons.append(person)
