import math

class Peg():
    def __init__(self, radius, theta, loom_index):
        """
        Constructor for the Peg class. Pegs are evenly-spaced points
        on the Loom circle.

        Parameters
        ----------
        radius : `float`
            radius of corresponding Loom
        theta : `int`
            counterclockwise angle (degrees) from positive x-axis
        loom_index : `int`
            the index for the peg about the Loom. (e.g. the maximum
            loom_index is Loom().num_pegs-1)
        """
        self.radius = radius
        self.theta = theta
        self.loom_index = loom_index
        self.x = self.get_x(radius, theta)
        self.y = self.get_y(radius, theta)

    def get_x(self, radius, theta):
        """
        Returns Euclidean x-coordinate of a point/peg.

        Parameters
        ----------
        radius : `float`
            radius of corresponding Loom
        theta : `int`
            counterclockwise angle (degrees) from positive x-axis
        """
        return radius*math.sin(math.radians(theta))

    def get_y(self, radius, theta):
        """
        Returns Euclidean y-coordinate of a point/peg.

        Parameters
        ----------
        radius : `float`
            radius of corresponding Loom
        theta : `int`
            counterclockwise angle (degrees) from positive x-axis
        """
        return radius*math.cos(math.radians(theta))
