# encoding=utf-8


"""第一题：编写程序，判断某天是某一年的第几天
# e.g. date: 2022-04-20
"""
import random


def q1(date):  # date:2022-04-20
    a = date.split('-')
    print(f'{a[0]}年{a[1]}月{a[2]}日')


'''第二题：鸡兔同笼问题。假设共有鸡、兔total只，脚leg只，求鸡、兔各有多少只
   返回一个元祖
'''


def q2(total, leg):
    x = total
    y = 0
    for i in range(total + 1):
        if 2 * x + 4 * y == leg:
            print(f'x = {x},y = {y}')
            return x, y
        else:
            x -= 1
            y += 1


'''第三题：编写程序，输出由6,7,8,9这四个数字组成的每位数都不相同的所有三位数
   将这些数字放在一个列表中返回
'''


def q3():
    a = []
    for i in range(6, 10):
        for j in range(6, 10):
            for k in range(6, 10):
                if i != j and j != k and i != k:
                    a.append(i * 100 + j * 10 + k)
    return a


'''第四题：生成一个含有m个随机数的列表，要求所有元素不相同，并且每个元素的值介于start到end之间
   作为列表返回
'''


def q4(m, start, end):
    return [random.randint(start, end) for i in range(m)]


'''第五题：计算个人所得税，输入每月工资，输出税费
应纳税所得额 = 工资 - 5000
每月应纳税额 = 应纳税所得额 * 适用税率 - 速算扣除数
级数	月度应纳税所得额		        税率（％）	速算扣除数
1		不超过3000元的				3			0
2		超过3000元至12000元的部分	    10			210
3		超过12000元至25000元的部分	20			1410
4		超过25000元至35000元的部分	25			2660
5		超过35000元至55000元的部分	30			4410
6		超过55000元至80000元的部分	35			7160
7		超过80000元的部分			45			15160
'''


# 12000, 12000-5000=7000, 3000*3%-0, 4000*10%-210
# 100000, 100000-5000=95000,


def q5(salary):
    if salary <= 5000:
        return 0
    elif salary <= 12000:
        return (salary - 5000) * 0.1
    elif salary <= 25000:
        return (salary - 12000) * 0.2 + 210
    elif salary <= 35000:
        return (salary - 25000) * 0.25 + 1410
    elif salary <= 55000:
        return (salary - 35000) * 0.3 + 2660
    elif salary <= 80000:
        return (salary - 55000) * 0.35 + 4410
    else:
        return (salary - 80000) * 0.45 + 15160


if __name__ == '__main__':
    # 下面是测试部分，根据前面的函数定义，自行设计测试数据，
    # 然后把下面函数调用中的下划线删除，替换为测试数据
    # 测试结果可能直接用print并无明显效果，可自行设计测试内容
    # 下面的测试代码只做个人验证使用，不作为考评依据
    print(q1("2022-12-10"))
    print(q2(10, 40))
    print(q3())
    print(q4(10, 10, 30))
    print(q5(10000))
