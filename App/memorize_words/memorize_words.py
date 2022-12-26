import random
from os import system

rand = []


# 获取[0~3]的随机数，作为选项
def get_random():
    global rand
    rand = random.sample(range(0, 4), 4)


# 获取正确选项的下标
def get_current():
    global rand
    index = 0
    for i in rand:
        if i == 0:
            return index
        else:
            index += 1


# 选择中文模式
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
        while True:
            user_input = input('输入选项：')
            if user_input.upper() != current:
                print('错误')
            else:
                break
        if pause:
            system('pause')
        system('cls')


# 选择英文模式
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
        while True:
            user_input = input('输入选项：')
            if user_input.upper() != current:
                print('错误')
            else:
                break
        if pause:
            system('pause')
        system('cls')
