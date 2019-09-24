# Write a small program to ask for a name and an age
# When both values have been entered, check if person
# is right age to on an 18-30 holiday (they must be over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print a polite message refusing the entry

# name = input("Please enter your name: ")
# age = int(input("Please enter your age: "))
# if 18 < age > 31:
#     print("You're eligible for Holiday trip for 18-30 days")
# else:
#     print("Stay back at home")

# Early computers could only perform add, Inorder to mul one num by another, they performed repeated addition.
# For eg, 5 * 8 was performed by adding 5 by 8 times
# 5 + 5 + 5 + 5 + 5 + 5 + 5 + 5 = 40
# Use a for loop, and augmented assignment, to give answer the result of mutliplying number by multiplier

number = 5
multiplier = 8
answer = 0

for i in range(multiplier):
    answer += number
    print("{} + ".format(number), end="\t")
