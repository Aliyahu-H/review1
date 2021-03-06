import json
import codecs


def check_inventory(_inventory, requirements):
    if len(requirements) == 0:
        return True
    _inv = {_inventory[i][0]: _inventory[i][1] for i in range(len(_inventory))}
    for i in range(len(requirements)):
        try:
            if _inv[requirements[i][0]] < requirements[i][1]:
                return False
        except KeyError:
            return False
    return True


def open_save_file():
    print('Введите путь к файлу сохранения:')
    save_way = input()
    print('Введите имя сохранения:')
    save_name = save_way + input() + '.txt'
    save_file = open(save_name)
    _save = json.load(save_file)
    save_file.close()
    return [_save['inventory'], _save['i'], _save['counter']]


def write_save_file(*args):
    print('Введите путь к файлу сохранения:')
    save_way = input()
    print('Введите имя сохранения:')
    save_name = save_way + input() + '.txt'
    save_file = open(save_name, 'w')
    _dict = {'i': args[0], 'counter': args[1], 'inventory': args[2]}
    json.dump(_dict, save_file, indent='\t')
    save_file.close()


pattern = codecs.open('resources/encoder_pattern.txt', "r", "utf_8_sig")
print(pattern.readline(), end='')
file_way = input()
print(pattern.readline(), end='')
file_name = file_way + input() + '.txt'
input_file = open(file_name)
quest = input_file.readlines()
graph = json.loads(quest[len(quest) - 1])
graph = {graph[i]: i for i in range(len(graph))}
print(pattern.readline(), end='')
print(pattern.readline(), end='')
inventory = list()
ans = input()
while True:
    if ans == '1':
        counter = 0
        i = 0
        break
    elif ans == '2':
        save = open_save_file()
        inventory = save[0]
        i = save[1]
        counter = save[2]
        break
    else:
        print('Error: there is not such option')
        ans = input()
while i < len(quest) - 1:
    current = json.loads(quest[i])
    print('//////////////////////////////////////////////////////////////////////////////////////////////////')
    description = current['description'].split('. ')
    for line in description:
        print(line + '.')
    print('//////////////////////////////////////////////////////////////////////////////////////////////////')
    if len(inventory) > 0:
        print('Инвентарь:')
        for line in inventory:
            print('\t' + line[0] + ': ' + str(line[1]))
        print('//////////////////////////////////////////////////////////////////////////////////////////////////')
    skip = 0
    not_skip = []
    for j in range(len(current['choice'][1])):
        if check_inventory(inventory, current['choice'][1][str(j + 1)]):
            print(str(j + 1 - skip) + ') ' + current['choice'][0][str(j + 1)])
            not_skip.insert(j - skip, j + 1)
        else:
            skip += 1
    print()
    s = input()
    pull = [str(x) for x in not_skip]
    while s not in pull and s != 's':
        print("Error: there is not such option")
        s = input()
    if s == 's':
        write_save_file(i, counter, inventory)
        continue
    user_choice = str(not_skip[int(s) - 1])
    print()
    if current['choice'][0][user_choice] == "Dead End":
        print("Игра окончена")
        break
    if current['choice'][0][user_choice] == "The End":
        break
    try:
        obj = current['choice'][2][user_choice]
        if len(obj) == 0:
            raise IndexError
        print('//////////////////////////////////////////////////////////////////////////////////////////////////')
        for _obj in obj:
            if _obj[1] > 0:
                print('\tВы получилили ' + _obj[0] + ': ' + str(_obj[1]))
            else:
                print('\tВы потеряли ' + _obj[0] + ': ' + str(-_obj[1]))
            inv = [inventory[i][0] for i in range(len(inventory))]
            if _obj[0] not in inv:
                inventory.insert(counter, _obj)
                counter += 1
            else:
                for k in range(len(inv)):
                    if inv[k] == _obj[0]:
                        inventory[k][1] += _obj[1]
                        if inventory[k][1] < 1:
                            del inventory[k]
                        break
    except IndexError:
        pass
    try:
        i = graph[current['neighbors'][current['choice'][0][user_choice]]]
        continue
    except KeyError:
        print('Graph out of range')
        break
pattern.close()
input_file.close()
