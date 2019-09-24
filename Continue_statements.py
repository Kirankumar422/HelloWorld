shopping_list = ["Milk", "Pasta", "Bread", "Spam", "Curd", "Rice"]
for item in shopping_list:
    if item == 'Spam':
        break
    print("Buy {} ".format(item))

nasty_food_item = ''
for item in shopping_list:
    if item == 'Spam':
        nasty_food_item = item
        break
if nasty_food_item:
    print("I don't want that {} ".format(nasty_food_item))
