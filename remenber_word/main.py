import random

from user.login import user_login
from user.register import user_register
from util import mydb


def remember_word(db: mydb.cjjdb, user_info: dict):
    words = db.get_words(user_info['current_plan'], user_info['goal_plan'])
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

if __name__ == '__main__':
    db = mydb.cjjdb()
    while True:
        user_in = input('login:1\n'
                        'register:2\n'
                        'exit:0\n'
                        'chosen:>')
        if user_in == '1':
            user_info = user_login(db)
            if user_info:
                remember_word(db, user_info)
            else:
                print('login fail, please confirm your id or password')


        elif user_in == '2':
            user_info = user_register(db)
            if user_info:
                print('your account info:')
                for k, v in user_info.items():
                    print(f'{k} --> {v}')
            else:
                print('you want to register username has been registered')


        elif user_in == '0':
            break


        else:
            print('err input')
