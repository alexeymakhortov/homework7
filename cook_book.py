# ЗАДАЧА 1

with open("recipes.txt", mode='r', encoding='UTF-8') as file:
    cook_book = {}
    while True:
        dish = file.readline().strip()  # название блюд
        if not dish:
            break

        test_list = []
        amount = int(file.readline().strip())  # количество ингредиентов
        while amount > 0:
            test_list.append(file.readline().strip().split(' | '))   # читаем ингредиенты
            amount -= 1

        ingredients_dish = []
        for line in test_list:
            ingredients_dish.append({'ingredient_name': line[0], 'quantity': line[1], 'measure': line[2]})

        file.readline()   # читаем пустую строку

        cook_book.setdefault(dish, ingredients_dish)

print(cook_book)


# ЗАДАЧА 2

def get_shop_list_by_dishes(dishes, person_count = 1):
    shop_list_dict = {}

    # ПЕРВЫЙ СЛУЧАЙ - передаем несколько блюд, но повторяющиеся ингредиенты перетираются

    for user_ingredients in dishes:
        user_ingredients2 = cook_book.get(user_ingredients)
        for dict_ingredients in user_ingredients2:
            ingredient_name = dict_ingredients['ingredient_name']
            ingredients_measure = dict_ingredients['measure']
            ingredients_quantity = int(dict_ingredients['quantity'])
            shop_list_dict.setdefault(ingredient_name, dict(measure = ingredients_measure, quantity = ingredients_quantity * person_count))
    print(shop_list_dict)


    # ВТОРОЙ СЛУЧАЙ - передаем одно блюдо

    get_ingredients = cook_book.get(dishes)
    for ingredients_dict in get_ingredients:
        test_ingredient_name = ingredients_dict['ingredient_name']
        test2_ingredient_name = ingredients_dict['measure']
        test3_ingredient_name = int(ingredients_dict['quantity'])
        shop_list_dict.setdefault(test_ingredient_name, dict(measure = test2_ingredient_name, quantity = test3_ingredient_name * person_count))
    print(shop_list_dict)

# get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2) # первый случай вывод
# get_shop_list_by_dishes('Омлет', 773)            # второй случай вывод










