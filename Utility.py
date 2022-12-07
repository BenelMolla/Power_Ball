"""
THESE TWO classes are represents the Lottery of powerball.
"""
import random

__author__ = "Benel_Molla"


# I created three  classes for create powerball lottery game
# and some packages

# This class is for white ball and power ball
class White_ball():
    def winner_white(self):  # White Balls and Black BAlls
        self.five_numbers = []
        self.winnerwhite = random.sample(range(1, 20), k=5)  # --here appends to five_numbers that takes 5 randomly
        self.five_numbers.append(self.winnerwhite)
        self.winnerwhite.sort()

    def power_ball(self):
        self.one_ball = []
        self.power_ball = random.choices(range(1, 10), k=1)
        self.one_ball.append(self.power_ball)                  # --here appends to one_ball that takes 1 randomly

        # This class is for lucky white and lucky power


class Lucky_white(White_ball):
    def white_lucky(self):
        self.lucky_box = []
        self.luckywhite1 = random.sample(range(1, 20), k=5)  # --here appends to lucky_box that takes 5 randomly
        self.lucky_box.append(self.luckywhite1)
        self.luckywhite1.sort()

    def lucky_power(self):
        self.lucky_ball = []
        self.lucky_power = random.choices(range(1, 10), k=1)  # --here appends to lucky_ball that takes 1 randomly
        self.lucky_ball.append(self.lucky_power)
