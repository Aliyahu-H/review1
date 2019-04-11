import codecs
pattern = codecs.open('resources/pattern.txt', "r", "utf_8_sig")
for i in range(4):
    print(pattern.readline(), end='')
pattern.close()
user_choice = input()
if user_choice == '1':
    from execute import encoder
elif user_choice == '2':
    from execute import maker
elif user_choice == '3':
    from execute import editor
else:
    print('Error: there is not such option')
