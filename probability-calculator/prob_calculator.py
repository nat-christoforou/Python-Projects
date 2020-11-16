"""A Probability Calculator."""


import copy
import random


class Hat:
    """
    A Hat object contains a number of balls of different colors.

    Parameters
    ----------
    **kwargs
        The keyword arguments are used for specifying the number of balls of
        each color that are in the hat object
    """

    def __init__(self, **kwargs):
        """Specify the number of balls of each color that are in the hat."""
        self.contents = [color for color, value in kwargs.items() for _ in range(value)]

    def draw(self, num_to_draw):
        """
        Remove balls at random from the hat and return those balls as a list of strings.

        Parameters
        ----------
        num_to_draw : int
            The amount of balls to draw from the hat

        Returns
        -------
        drawn
            A list of the balls that are drawn
        """
        if num_to_draw >= len(self.contents):
            return self.contents

        drawn = []
        for _ in range(num_to_draw):
            random_ball = random.choice(self.contents)
            drawn.append(random_ball)
            self.contents.remove(random_ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Determine the probability of getting the expected_balls from a hat \
    by performing num_experiments experiments.

    Parameters
        ----------
        hat : object
            A hat object containing balls
        expected_balls : dictionary
            The exact group of balls to attempt to draw from the hat for the experiment
        num_balls_drawn : int
            The number of balls to draw out of the hat in each experiment
        num_experiments : int
            The number of experiments to perform

        Returns
        -------
        probability
            the probability of getting the expected_balls from a hat
    """
    successes = 0

    for _ in range(num_experiments):
        temp = copy.deepcopy(hat)
        balls_drawn = temp.draw(num_balls_drawn)
        if all(balls_drawn.count(ball) >= expected_balls[ball] for ball in expected_balls.keys()):
            successes += 1

    probability = successes / num_experiments
    return probability
