class Bounce:
    def __init__(self, rounds=10, occurrence=1, required_points=1):
        self.rounds = rounds
        self.occurrence = occurrence
        self.required_points = required_points
        self._trajectory = False
        self.current_trajectory = 0
        self.valid_points = 0
        self.remaining_points = self.occurrence
        self.ready_to_trade = False

    @property
    def trajectory(self):
        return self._trajectory

    @trajectory.setter
    def trajectory(self, _trajectory):
        if _trajectory:
            self.current_trajectory += _trajectory
        if _trajectory * self.current_trajectory > 0:
            self.remaining_points -= 1
            #print(self.required_points)
        if self.remaining_points <= 0:
            self.valid_points += 1
            self.remaining_points = self.occurrence
        if self.valid_points >= self.remaining_points:
            if self.trajectory < 0:
                self.ready_to_trade = True

        self._trajectory = _trajectory
