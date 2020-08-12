from pprint import pprint

def get_cook_book(file_name):
    result = {}
    with open(file_name, mode='r', encoding='UTF-8') as file:
        while True:
            dish = file.readline().strip()  # название блюд
            if not dish:
                break

            test_list = []
            amount = int(file.readline().strip())  # количество ингредиентов
            while amount > 0:
                test_list.append(file.readline().strip().split(' | '))  # читаем ингредиенты
                amount -= 1

            ingredients_dish = []
            for line in test_list:
                ingredients_dish.append({'ingredient_name': line[0], 'quantity': line[1], 'measure': line[2]})

            file.readline()  # читаем пустую строку

            result.setdefault(dish, ingredients_dish)
        return result

# pprint(get_cook_book("recipes.txt"))


# ЗАДАЧА 2

def get_shop_list_by_dishes(dishes, cook_book, person_count=1):
    result = {}

    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                quantity = int(ingredient['quantity'])
                measure = ingredient['measure']
                if name in result:
                    quantity = result[name]['quantity'] + quantity * person_count
                    result[name]['quantity'] = quantity
                else:
                    result[name] = {'measure': measure, 'quantity': quantity * person_count}

    return result

if __name__ == '__main__':
    cook_book = get_cook_book('recipes.txt')
    result = get_shop_list_by_dishes(['Омлет', 'Фахитос'], cook_book, 2)  # первый случай вывод
    # pprint(result)
'''
{
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}
'''
