import json
import codecs

graph = list()
n = 0


def make_list(a):
    if type(a) == list:
        for j in range(len(a)):
            a[j] = a[j].split(', ')
            a[j][1] = int(a[j][1])
    else:
        a = a.split(', ')
        a[1] = int(a[1])
        a = [a]
    return a


def add_room(file):
    global graph
    global n
    print('Введите название локации:')
    room_name = input()
    graph.insert(n, room_name)
    n += 1
    print('Введите описание локации:')
    description = input()
    choice = add_choices()
    print('Введите имена связанных локаций, разделяя их ";":')
    adjacent_rooms = input().split('; ')
    print('Введите условия для перехода из локации '
          'в том же порядке, разделяя их ";":')
    conditions = input().split('; ')
    neighbors = []
    for i in range(len(conditions)):
        neighbors.insert(i, (adjacent_rooms[i], conditions[i]))
    neighbors = {x: y for (y, x) in neighbors}
    obj = {'room_name': room_name,
           'description': description,
           'choice': choice,
           'neighbors': neighbors}
    json.dump(obj, file)
    file.write('\n')
    print('Success room addition')


def add_choices():
    choices = []
    requirements = []
    stuff = []
    print('Введите количество выборов:')
    number = int(input())
    for i in range(number):
        print('Введите выбор:')
        choices.insert(i, (i + 1, input()))
        print('Введите требования для него:')
        r = input()
        if len(r) > 0:
            r = make_list(r.split('; '))
        requirements.insert(i, (i + 1, r))
        print('Введите получаемые предметы:')
        s = input()
        if len(s) > 0:
            s = make_list(s.split('; '))
        stuff.insert(i, (i + 1, s))
    choices = {x: y for (x, y) in choices}
    requirements = {x: y for (x, y) in requirements}
    stuff = {x: y for (x, y) in stuff}
    return choices, requirements, stuff


pattern = codecs.open('resources/editor_pattern.txt', "r", "utf_8_sig")
print(pattern.readline(), end='')
file_way = input()
print(pattern.readline(), end='')
file_name = file_way + input() + '.txt'
input_file = open(file_name, 'r')
current = input_file.readlines()
graph = json.loads(current[len(current) - 1])
current = current[:-1]
n = len(current)
input_file.close()
output = open(file_name, 'w')
output.writelines(current)
variants = pattern.readline().split(',, ')
flag = True
while flag:
    for line in variants:
        print(line)
    current = int(input())
    if current == 1:
        add_room(output)
    elif current == 2:
        flag = False
    else:
        print('Error: there is not such option')
json.dump(graph, output)
output.close()
pattern.close()
