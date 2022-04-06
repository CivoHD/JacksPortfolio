# ALL CHOICES
# USER AND COMPUTER
# R P S
# WINNING/ LOSING/ DRAWING
import random


class RPS:

    def game():
        while True:
            computer = random.randint(1, 3)
            user = int(input(" Rock = 1 | Paper = 2 | Sissors = 3 "))

            if user == computer:
                print(f"You both have chosen {user} its a tie!!")
                RPS.tryAgain()
                break
            elif user == 1 and computer == 3:
                print("Rock beats Sissors  you win!!")
                RPS.tryAgain()
                break
            elif user == 2 and computer == 1:
                print("Paper beats Rock you win!!")
                RPS.tryAgain()
                break
            elif user == 3 and computer == 2:
                print("Sissors beats Paper you win!!")
                RPS.tryAgain()
                break
            elif user == 1 and computer == 2:
                print("Papper beats Rock you lose!!")
                RPS.tryAgain()
                break
            elif user == 2 and computer == 3:
                print("Sissors beats Paper you lose!!")
                RPS.tryAgain()
                break
            elif user == 3 and computer == 1:
                print("Rock beats Sissors you lose!!")
                RPS.tryAgain()
                break
            else:
                print("Invalid input try again")

    def tryAgain():
        user = input("Do you want to play again (Y or N) ")
        if user == 'y':
            RPS.game()
        else:
            print("Goodbye!!")


def main():
    RPS.game()


main()
