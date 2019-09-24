number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        # cleanedNumber = cleanedNumber + number[i]
        cleanedNumber = number[i]  # Augmented Assignment you can use all arithmetic operators

newNumber = int(cleanedNumber)
print("The number is {} ".format(newNumber))

x = 23
x += 1  # We can use all the arithmetic operators
print(x)

greeting = "Good "
greeting += "Evening "
print(greeting)

greeting *= 5
print(greeting)  # These are the two operators used for strings

