# for i in range(1, 12):
#     print("No {} squared is {} and cubed is {:4}".format(i, i**2, i**4))
#     print("Calculation completed")
#     print("Try again")

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess != 5:
    if guess <5:
        print("Please guess higher")
    else: #guess must be greater than 5
        print("Please guess lower")

    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")