# for a in range(1, 20):
#     print("a is now {}".format(a))

number = "9, 223, 372, 036, 854, 775, 807"
cleanedNumber = ''

# for i in range(0, len(number)):
#     print(number[i])

for i in range(0, len(number)):
    if number[i] in '0123456789':
        # print(number[i], end='')
        cleanedNumber = cleanedNumber + number[i]
newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))