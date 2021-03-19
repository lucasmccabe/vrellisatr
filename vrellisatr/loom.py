from peg import Peg
import matplotlib.pyplot as plt


class Loom():
    def __init__(self, num_pegs = 200, radius = 100):
        """
        Constructor for the Loom class. A Loom is a circle of `num_pegs` pegs.

        Parameters
        ----------
        num_pegs : `int`
            the number of pegs to arrange
        radius : `int`
            radius of the Loom / how big you want it to be
        """
        self.num_pegs = num_pegs
        self.pegs = {
            loom_index: Peg(radius = radius,
                theta = loom_index*360/num_pegs,
                loom_index = loom_index) \
            for loom_index \
            in range(num_pegs)}

    def plot(self):
        """
        Plots the Loom points.

        Parameters
        ----------
        None
        """
        x = [self.pegs[i].x for i in range(self.num_pegs)]
        y = [self.pegs[i].y for i in range(self.num_pegs)]
        plt.scatter(x, y, color = "black")
        plt.axis("square")
        plt.show()
        return None
