from Lift import Lift


class LiftController:

    def __init__(self, lifts_list):
        self.lifts = []
        if type(lifts_list[0]) is list:
            for x in lifts_list:
                self.lifts.append(Lift(x))
        else:
            self.lifts.append(Lift(lifts_list))
        self.total_distance = 0

    def get_closest_lift(self, requesting_floor):
        selected_lift = self.lifts[0]
        for lift in self.lifts:
            if abs(requesting_floor - lift.position) < abs(requesting_floor - selected_lift.position):
                selected_lift = lift

        return selected_lift

    def move_lift(self, lift, requesting_floor, target_floor):
        self.total_distance += abs(lift.position - requesting_floor) + abs(requesting_floor - target_floor)
        lift.position = target_floor
