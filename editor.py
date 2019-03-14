import json


def add_room(file):
    print('Введите название локации:')
    room_name = input()
    print('Введите описание локации:')
    description = input()
    choice = add_choices()
    print('Введите имена связанных локаций через запятую:')
    adjacent_rooms = input().split(', ')
    print('Введите условия для перехода из локации в том же порядке через запятую:')
    conditions = input().split(', ')
    neighbors = []
    for i in range(len(conditions)):
        neighbors.insert(i, (adjacent_rooms[i], conditions[i]))
    neighbors = {x: y for (y, x) in neighbors}
    obj = {'room_name': room_name, 'description': description, 'choice': choice, 'neighbors': neighbors}
    json.dump(obj, file)
    print('Success room addition')


def add_choices():
    choices = []
    requirements = []
    print('Введите количество выборов:')
    number = int(input())
    for i in range(number):
        print('Введите выбор:')
        choices.insert(i, (i + 1, input()))
        print('Введите требования для него:')
        requirements.insert(i, (i + 1, input()))
    choices = {x: y for (x, y) in choices}
    requirements = {x: y for (x, y) in requirements}
    return choices, requirements


pattern = open('editor_pattern.txt')
print(pattern.readline(), end='')
file_way = input()
print(pattern.readline(), end='')
file_name = file_way + input() + '.txt'
output = open(file_name, 'w')
variants = pattern.readline().split(',, ')
flag = True
while flag:
    for line in variants:
        print(line)
    current = int(input())
    if current == 1:
        add_room(output)
    if current == 2:
        pass
    if current == 3:
        flag = False
output.close()

