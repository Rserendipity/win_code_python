import random
from os import system

rand = []


def get_random():
    global rand
    rand = random.sample(range(0, 4), 4)


def get_current():
    global rand
    index = 0
    for i in rand:
        if i == 0:
            return index
        else:
            index += 1


def choose_chinese(word_info, pause):
    global rand
    option = ['A', 'B', 'C', 'D']

    for word in word_info:
        get_random()
        print('这个单词是：' + word[0])
        s = ''
        for index in range(0, 4):
            s += option[index]
            s += '：'
            s += word[rand[index] + 4]
            s += '\n'
        print(s)
        current = option[get_current()]
        while input('输入选项：') != current:
            print('错误')
        if pause:
            system('pause')
        system('cls')


def choose_english(word_info, pause):
    global rand
    option = ['A', 'B', 'C', 'D']

    for word in word_info:
        get_random()
        print('这个单词是：' + word[4])
        s = ''
        for index in range(0, 4):
            s += option[index]
            s += '：'
            s += word[rand[index]]
            s += '\n'
        print(s)
        current = option[get_current()]
        while input('输入选项：') != current:
            print('错误')
        if pause:
            system('pause')
        system('cls')
