# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1
#
# available_exists = ["east", "north east", "south"]
#
# chosen_exit = ''
# while chosen_exit not in available_exists:
#     chosen_exit = input("Please choose a exit direction: ")
#     if chosen_exit == "quit":
#         print("Game Over")
#         break
# else:
#     print("Aren't you glad you got out of there!")

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:  # guess must be greater than number
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")