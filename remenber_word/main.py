import random

from os import system
from user.login import user_login
from user.register import user_register
from util import mydb


def remember_word(db: mydb.cjjdb, user_info: dict):
    words = db.get_words(user_info['current_plan'], user_info['goal_plan'])
    abcd_to_1234 = {'A': 1, 'a': 1, 'B': 2, 'b': 2, 'C': 3, 'c': 3, 'D': 4, 'd': 4, '1': 1, '2': 2, '3': 3, '4': 4}
    en_list = [1, 2, 3, 4]

    for word in words:
        random.shuffle(en_list)
        index = en_list.index(1) + 1
        while True:
            system('cls')
            print(f'中文: {word[0]}'
                  f'A:{word[en_list[0]]}'
                  f'B:{word[en_list[1]]}'
                  f'C:{word[en_list[2]]}'
                  f'D:{word[en_list[3]]}')
            user_in = input('你的选择:>')
            if user_in == 'A' or user_in == 'a' or user_in == '1':
                user_in_num = abcd_to_1234[user_in]
            elif user_in == 'B' or user_in == 'b' or user_in == '2':
                user_in_num = abcd_to_1234[user_in]
            elif user_in == 'C' or user_in == 'c' or user_in == '3':
                user_in_num = abcd_to_1234[user_in]
            elif user_in == 'D' or user_in == 'd' or user_in == '4':
                user_in_num = abcd_to_1234[user_in]
            else:
                print('不正确的输入.')
                system('pause')
                continue
            if user_in_num == index:
                print('正确!')
                if user_info['is_pause']:
                    system('pause')
                break
            else:
                print('答案错误!')
                system('pause')


if __name__ == '__main__':
    db = mydb.cjjdb()
    while True:
        user_in = input('登录:1\n'
                        '注册:2\n'
                        '退出:0\n'
                        'chosen:>')
        if user_in == '1':
            user_info = user_login(db)
            if user_info:
                remember_word(db, user_info)
                print('你已完成本轮单词')
                db.update_plan(user_info)
                print('已经上传进度')
                system('pause')
                system('cls')
            else:
                print('登录失败, 请检查用户名是否存在 或 密码是否正确')


        elif user_in == '2':
            user_info = user_register(db)
            if user_info:
                system('cls')
                print('你的账号信息:')
                for k, v in user_info.items():
                    print(f'{k} --> {v}')
                system('pause')
                system('cls')
            else:
                print('该账户已被注册')
                system('pause')
                system('cls')


        elif user_in == '0':
            break


        else:
            print('不正确的输入.')
