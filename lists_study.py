# ipAddress = input("Please enter IP Address: ")
# print(ipAddress.count("."))

# parrot_list = ["non pinin'", "no more", "a stiff", "bereft of live"]
# parrot_list.append("A Norwegian Blue")
# for i in parrot_list:
#     print("The parrot is {}".format(i))
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]

# numbers = even + odd
# numbers.sort()
# print(numbers)
# numbers_in_order = sorted(numbers)
# print(sorted(numbers))
# print(numbers_in_order)
#
# if numbers == numbers_in_order:
#     print("The lists are equal")
# else:
#     print("The lists are not equal")
#
# if numbers_in_order == sorted(numbers):
#     print("The lists are equal")
# else:
#     print("The lists are not equal")


# lists can be created by using square phrases

# list_1 = []   # Empty list is created
# list_2 = list()   # This the another way to create a empty list; list constructor
#
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("Both lists are equal")
#
# print(list("Hi Kiran"))


#
# another_even = list(even)
# another_even = sorted(even, reverse=True)
# print(another_even is even)
# print(another_even == even)
# another_even.sort(reverse=True)
# print(even)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for i in numbers:
    print(i)

    for j in i:
        print(j)
