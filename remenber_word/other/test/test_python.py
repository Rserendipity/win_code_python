import random

# en_list = [1, 2, 3, 4]
# random.shuffle(en_list)
# print(en_list)
# print(en_list.index(1) + 1)

# words = db.get_words(user_info['current_plan'], user_info['goal_plan'])
words = [('vt. 提醒；使想起\n', 'remind\n', 'map\n', 'insight\n', 'accompany\n'),
         ('n. 劈开；裂缝 adj. 劈开的 vt. 分离；使分离；劈开；离开；分解 vi. 离开；被劈开；断绝关系\n', 'split\n', 'generous\n',
          'goat\n', 'exclaim\n'),
         ('adj. 成熟的；充分考虑的；到期的；成年人的 vi. 成熟；到期 vt. 使…成熟；使…长成；慎重作出\n', 'mature\n', 'pants\n',
          'handful\n', 'punctual\n')]

abcd_to_1234 = {'A': 1, 'a': 1, 'B': 2, 'b': 2, 'C': 3, 'c': 3, 'D': 4, 'd': 4}
en_list = [1, 2, 3, 4]
for word in words:
    random.shuffle(en_list)
    index = en_list.index(1) + 1
    while True:
        print(f'Chinese is {word[0]}'
              f'A:{word[en_list[0]]}'
              f'B:{word[en_list[1]]}'
              f'C:{word[en_list[2]]}'
              f'D:{word[en_list[3]]}')
        user_in = input('your chose:>')
        if user_in == 'A' or user_in == 'a':
            user_in_num = abcd_to_1234[user_in]
        elif user_in == 'B' or user_in == 'b':
            user_in_num = abcd_to_1234[user_in]
        elif user_in == 'C' or user_in == 'c':
            user_in_num = abcd_to_1234[user_in]
        elif user_in == 'D' or user_in == 'd':
            user_in_num = abcd_to_1234[user_in]
        else:
            print('err input')
            continue
        if user_in_num == index:
            print('current!')
            break
        else:
            print('err')
