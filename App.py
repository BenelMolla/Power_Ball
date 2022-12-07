from Utility import White_ball
from Utility import Lucky_white
from colorama import Fore, Back, Style
import emoji


class Grading(Lucky_white):
    def show(self):
        Lucky_white.lucky_power(self)

        White_ball.winner_white(self)
        White_ball.power_ball(self)
        Lucky_white.white_lucky(self)
        Lucky_white.lucky_power(self)

        # here  prints winnerwhite and power_ball
        # and prints luckywhite1 and lucky_power

        print("today's Powerball winning numbers")
        print(Fore.LIGHTMAGENTA_EX, *self.winnerwhite, Fore.RESET, Fore.YELLOW, *self.power_ball, Fore.RESET)
        print("Your lucky numbers are")
        print(Fore.LIGHTMAGENTA_EX, *self.luckywhite1, Fore.RESET, Fore.YELLOW, *self.lucky_power, Fore.RESET)

    def grade(self):

        """
        here display how count works
         and print

        """
        count = 0
        countW = 0
        if self.power_ball == self.lucky_power:
            count = count + 1
        print("the amount of power ball is", count)
        for y in self.luckywhite1:
            if y in self.winnerwhite:
                countW = countW + 1
        print("the amount of white ball is", countW)
        print("==================================================")

        # here Prints the value of what the player got if he won , otherwise print try again message.
        # prints the value of white-ball and the value of powerball
        # and there are some emojis those display

        if countW == 5 and count == 1:
            print(Fore.GREEN, "5 correct white balls, powerball: $324,000,000", Fore.RESET)
            print(emoji.emojize(' :thumbs_up:'))
        elif countW == 5 and count == 0:
            print(Fore.LIGHTGREEN_EX, "5 correct white balls, but no powerball: $1,000,000", Fore.RESET)
            print(emoji.emojize(' :thumbs_up:'))
        elif countW == 4 and count == 1:
            print(Fore.LIGHTGREEN_EX, "4 correct white balls, and powerball: $10,000", Fore.RESET)
            print(emoji.emojize(' :thumbs_up:'))
        elif countW == 4 and count == 0:
            print(Fore.LIGHTGREEN_EX, "4 correct white balls, but no powerball: $100", Fore.RESET)
            print(emoji.emojize(' :thumbs_up:'))
        elif countW == 3 and count == 1:
            print(Fore.LIGHTGREEN_EX, "3 correct white balls and  powerball: $100", Fore.RESET)
            print(emoji.emojize(' :thumbs_up:'))
        elif countW == 3 and count == 0:
            print(Fore.LIGHTCYAN_EX, "3 correct white balls, but no powerball: $7", Fore.RESET)
            print(emoji.emojize(' :thumbs_up:'))
        elif countW == 2 and count == 1:
            print(Fore.LIGHTCYAN_EX, "2 correct white balls and powerball: $7", Fore.RESET)
            print(emoji.emojize(' :thumbs_up:'))
        elif countW == 1 and count == 1:
            print(Fore.LIGHTBLUE_EX, "1 correct white balls and powerball: $ 4", Fore.RESET)
            print(emoji.emojize(' :thumbs_up:'))
        elif countW == 0 and count == 1:
            print(Fore.LIGHTBLUE_EX, "No white balls, Just powerball: $ 4", Fore.RESET)
            print(emoji.emojize(' :thumbs_up:'))
        else:
            print(Fore.RED + "try again" + Fore.RESET)
            print(emoji.emojize("\U0001F923"))


ben = White_ball()
ben.winner_white()  # here the function part for white-ball class
ben.power_ball()

boss = Lucky_white()
boss.white_lucky()  # here the function part for luckywhite class
boss.lucky_power()

lun = Grading()
lun.show()  # here the function part for grading class
lun.grade()
