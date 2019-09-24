fruits = { "Orange": "a sweet, orange, citrus fruit",
            "apple": "good for making cider",
            "lemon": "a sour, yellow citrus fruit",
            "grape": "a small, sweet fruit growing in bunches",
            "lime": "a sour, green citrus fruit"}
# print(fruits)
# print(fruits["Orange"])
# fruits["pear"] = "an odd shaped apple"
# print(fruits)
# fruits["pear"] = "great with tequalia"
# print(fruits)
# del fruits["lemon"]
# print(fruits)
# # del fruits
# print(fruits)
# fruits.clear()
# print(fruits)
# print(fruits["tomata"])
# bike = {"make": "Honda", "model": ""}

print(fruits)
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     # description = fruits.get(dict_key, "We don't have a {}".format(dict_key))
#     # print(description)
#     if dict_key in fruits:
#         description = fruits.get(dict_key)
#         print(description)
#     else:
#         print("We don't have a {}".format(dict_key))
#
# for snack in fruits:
#     print(fruits[snack])

# for i in range(10):
#     for snack in fruits:
#         print( "{} is {}".format(snack, fruits[snack]))
#     print("=" * 40)

# ordered_keys = list(fruits.keys())
# # ordered_keys.sort()
# ordered_keys = sorted(list(fruits.keys()))
# for f in ordered_keys:
#     print("{} - {}".format(f, fruits[f]))
#
# # for f in sorted(fruits.keys()):
# for f in fruits:
#     print("{} - {}".format(f, fruits[f]))

# for val in fruits.values():
#     print(val)
#
# print("-" * 40)
# for key in fruits:
#     print(fruits[key])


# fruits_keys = fruits.keys()
# print(fruits.keys())

# print(fruits.values())
# fruits["tomato"] = "not nice with ice cream"
# print(fruits_keys)

print(fruits)
print(fruits.items())
f_tuple = tuple(fruits.items())
print(f_tuple)


for snack in f_tuple:
    item, description = snack
    print("{} is {}".format(item, description))

print(dict(f_tuple))