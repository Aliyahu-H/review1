import json

pattern = open('encoder_pattern.txt')
print(pattern.readline(), end='')
file_way = input()
print(pattern.readline(), end='')
file_name = file_way + input() + '.txt'
input_file = open(file_name)
quest = input_file.readlines()
graph = json.loads(quest[len(quest) - 1])
graph = {graph[i]: i for i in range(len(graph))}
inventory = list()
counter = 0
i = 0
while i < len(quest) - 1:
    current = json.loads(quest[i])
    print(current['room_name'])
    description = current['description'].split('. ')
    for line in description:
        print(line + '.')
    if len(inventory) > 0:
        print('Инвентарь:')
        for line in inventory:
            print(line[0] + ': ' + str(line[1]))
    for j in range(len(current['choice'][1])):
        print(str(j + 1) + ') ' + current['choice'][0][str(j + 1)])
    print()
    user_choice = input()
    if current['choice'][0][user_choice] == "Dead End":
        print("Game Over")
        break
    try:
        obj = current['choice'][2][user_choice].split(', ')
        if len(obj) < 2:
            raise KeyError
        if int(obj[1]) > 0:
            print('Вы подобрали ' + obj[0] + ': ' + obj[1])
        else:
            print('Вы потеряли ' + obj[0] + ': ' + obj[1])
        inv = [inventory[i][0] for i in range(len(inventory))]
        obj[1] = int(obj[1])
        if obj[0] not in inv:
            inventory.insert(counter, obj)
            counter += 1
        else:
            for k in range(len(inv)):
                if inv[k] == obj[0]:
                    inventory[k][1] += obj[1]
                    if inventory[k][1] < 1:
                        del inventory[k]
                    break
    except KeyError:
        pass
    try:
        i = graph[current['neighbors'][current['choice'][0][user_choice]]]
        continue
    except KeyError:
        print('Graph out of range')
        break
