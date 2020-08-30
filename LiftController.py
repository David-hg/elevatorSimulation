from Lift import Lift


class LiftController:

    def __init__(self, lifts_list):
        self.lifts = []
        if type(lifts_list[0]) is list:
            for x in lifts_list:
                self.lifts.append(Lift(x))
        else:
            self.lifts.append(Lift(lifts_list))

    def get_closest_lift(self, requesting_floor):
        selected_lift = self.lifts[0]
        for lift in self.lifts:
            if abs(requesting_floor - lift.position) < abs(requesting_floor - selected_lift.position):
                selected_lift = lift

        return selected_lift

    def move_lift(self, lift, requesting_floor, target_floor):
        lift.total_distance += abs(lift.position - requesting_floor) + abs(requesting_floor - target_floor)
        lift.position = target_floor

    def get_experiment_results(self):
        total_simulation_distance = 0
        i = 0
        for lift in self.lifts:
            print("Lift " + str(i) + " with stops in " + str(lift.floors) + ": " + lift.total_distance)
            total_simulation_distance += lift.total_distance
            i += 1
        print(total_simulation_distance)