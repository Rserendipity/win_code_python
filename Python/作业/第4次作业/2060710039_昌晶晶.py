import random

# 1.统计单词出现的次数
f = open('./cnnnews.txt', 'r')
x = f.read().split()  # 读取数据,然后去掉空白符
print(x)
a = []
for i in x:
    a.append(i.replace('\'', '').replace('\"', '').replace('.', '').replace(',', '').lower())  # 去掉 ' " . , 符号并转为纯小写字母
d = dict()
for i in a:
    d[i] = d.get(i, 0) + 1
y1 = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}  # 排序
# print(y1)


# 2.生成0~100之间的数,并去重
L1 = random.sample(range(0, 101), 101)  # 方法一
S = set()  # 方法二
L2 = list()
for i in range(0, 101):
    while True:
        temp = random.randint(0, 100)
        if temp not in S:
            L2.append(temp)
            S.add(temp)
            break
# print(L2)


# 3.字典列表排序
L3 = [{'name': 'Dong', 'age': 37}, {'name': 'Zhang', 'age': 40}, {'name': 'Li', 'age': 50}, {'name': 'Dong', 'age': 43}]
L3.sort(key=lambda x: (x['name'], int(str(x['age'])[0]) + int(str(x['age'])[1])))
# print(L3)
