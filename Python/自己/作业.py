def q1(s):
    pos = s[::]
    revers = s[::-1]
    if pos == revers:
        return True
    else:
        return False


def q2(lst):
    a = lst[:]
    a.sort()
    del a[-1]
    temp = a[0]
    del a[0]
    a.append(temp)
    return a


def q3(s):
    my_str = s.lower().split(' ')
    d = dict()
    for i in my_str:
        d[i] = d.get(i, 0) + 1
    my_list = []
    for k in d.keys():
        if d[k] >= 2:
            my_list.append(k)
            my_list.append(d[k])
    return my_list


def q4(num):
    my_list = list(str(num))
    s = 0
    for i in range(len(my_list)):
        s += int(my_list[i])
    return s


def q5():
    listYear = [x for x in range(1900, 2022) if x % 100 != 0 and x % 4 == 0]
    return listYear


def q6(d):
    my_list = d.split('-')
    return str(int(my_list[1])) + '/' + str(int(my_list[2])) + '/' + my_list[0]


def q7(folder):
    import os
    listFile = [x for x in os.listdir(fr'{folder}')]
    return [listFile[i] for i in range(1, len(listFile)) if str(listFile[i]).endswith(('.exe', '.py'))]


def q8(n):
    import random
    a = [str(random.randint(0, 9)) for i in range(n)]
    return ''.join(a)


def q9(dictList):
    dictList.sort(key=lambda x: (x['name'], int(str(x['age'])[0]) + int(str(x['age'])[1])))
    return dictList


def q10(amount, count):
    import random
    a = [random.randint(1, count) for i in range(count)]
    return [round(a[i] / 1.0 / sum(a) * amount, 2) for i in range(count)]


print(q3('Python is python I love is is'))
print(q10(10, 10))

print(round(100.2341234213, 4))

a = str(10.023234).split('.')[0] + '.' + str(10.023234).split('.')[1][:2]
print(a)

