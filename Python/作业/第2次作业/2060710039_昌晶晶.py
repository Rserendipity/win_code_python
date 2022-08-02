import random

userInput = input("请输入红包个数:>")

a = [random.randint(1, 100) for i in range(int(userInput))]

print(a)

print('max =', max(a), 'min =', min(a), 'sum =', sum(a), 'arge =', sum(a) * 1.0 / len(a))


