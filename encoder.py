import json

pattern = open('encoder_pattern.txt')
print(pattern.readline(), end='')
file_way = input()
print(pattern.readline(), end='')
file_name = file_way + input() + '.txt'
input_file = open(file_name)
current = json.load(input_file)
print(current['room_name'])
print(current['description'])
for i in range(len(current['choice'][1])):
    print(str(i + 1) + ') ' + current['choice'][0][str(i + 1)])
print()
user_choice = input()
print(current['neighbors'][user_choice])
