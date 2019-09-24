number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for char in number:
    if  char in '0123456789':
        cleanedNumber = cleanedNumber + char
newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ["not pinin'", "no more", "a stiff", "bereft of life"]:
    print("This parrot is {}".format(state))
    # print("This parrot is " + state)

for i in range(0, 100, 10):
    print("i is {} ".format(i))

for i in range(1, 11):
    for j in range(1, 11):
        print("{0} * {1} = {2} ".format(i, j, i * j), end="\t")
    #print("-*-*-*-*-*-*-*-*-*")

