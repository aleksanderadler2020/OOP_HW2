from pprint import pprint

# Задача №1
cook_book = {}
with open('recipes.txt') as f:
    while True:
        dish = f.readline().replace('\n', '')
        if dish == '':  # Конец файла
            break
        ing_count = int(f.readline())
        cook_book[dish] = []
        for i in range(ing_count):
            ing = f.readline().split('|')
            cook_book[dish].append({'ingredient_name': ing[0], 'quantity': int(ing[1].replace(' ', '')),
                                    'measure': ing[2].replace('\n', '')})
        f.readline()

print('Задача №1')
pprint(cook_book)
print()


def get_shop_list_by_dishes(dishes, person_count):
    ingridients = {}
    for dish in dishes:
        for ing in cook_book[dish]:
            if ing['ingredient_name'] in ingridients.keys():
                ingridients[ing['ingredient_name']]['quantity'] += ing['quantity'] * person_count
            else:
                ingridients[ing['ingredient_name']] = {'measure': ing['measure'],
                                                       'quantity': ing['quantity'] * person_count}
    return ingridients


print('Задача №2')
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print()

file_line_size = {}
with open('1.txt') as f:
    file_line_size['1.txt'] = len(f.read().split('\n'))
with open('2.txt') as f:
    file_line_size['2.txt'] = len(f.read().split('\n'))
with open('3.txt') as f:
    file_line_size['3.txt'] = len(f.read().split('\n'))


sort_file_list = sorted(file_line_size.items(), key=lambda item: item[1])

with open('result.txt', 'w') as wf:
    for file_name, file_line_count in sort_file_list:
        wf.writelines(file_name)
        wf.writelines('\n')
        wf.writelines(str(file_line_count))
        wf.writelines('\n')
        with open(file_name, 'r') as rf:
            wf.write(rf.read())
        wf.writelines('\n')

print('Задача №3')
with open('result.txt') as rf:
    print(rf.read())


class context_manager:
    def __enter__(self):
        print('Вошли')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Вышли')


test = context_manager()
print('Задача №4')
with test:
    pass
