from random import choice


class MolecularMotion:
    def __init__(self, num_of_points=5000):
        self.num_of_points = num_of_points

        # For any random motion, it begins from (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_of_points:
            x_step = self._get_xstep()
            y_step = self._get_ystep()

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
            
            
    # Making use of hepler methods
    def _get_xstep(self):
        """Returns the distance moved through the x-axis"""
        x_direction = choice([-1,1])
        x_distance = choice([1, 2, 3, 4, 5])
        return x_direction * x_distance

    def _get_ystep(self):
        """Returns the distance moved through the y-axis"""
        y_direction = choice([-1, 1])
        y_distance = choice([1, 2, 3, 4, 5])
        return y_direction * y_distance



