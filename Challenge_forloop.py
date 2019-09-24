# # Write a program to print out the capitals letters in the string
#
# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, Irrigation, Roads,
# the Fresh-Water System, and Public Health, what have the Romans ever done for us ?"""
#
# for char in quote:
#     if char in 'ASMEWPOIRFHR':
#         print(char)
#
# # Write a program to print out all the numbers from 0 to 100 that are divisible by 7
#
# for i in range(0, 101):
#     if (i % 7 == 0):
#         print(i)

# Print numbers from 0 to 99 with added 7 and need to break code once the values reaches to remainder 0 with divisible by 11

# for i in range(0, 100, 7):
#     print(i)
#     if i > 0 and i % 11 == 0:
#         break

# Write a program to print out all the numbers from 0 to 20 that aren't divisible by 3 or 5.
# Zero is considered divisible by everything(Zero should not be in your output)
# The aim is to use the continue statement, but it's also possible to do this without continue.


for i in range(1, 21):
    # print(i)
    if i % 3 == 0 or i % 5 == 0:
        continue
    #if i % 5 == 0:
     #   continue
    print(i)



