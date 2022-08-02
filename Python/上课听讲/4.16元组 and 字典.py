import random
import string

a = [1, 2, 3, 4]  # 列表
'''
    列表可以修改
    使用list()可以把其他的类型更改为列表
    列表不可以做为字典的key,因为列表是可变的
'''
b = (1, 2, 3, 4)  # 元组
'''
    元组不可修改
    使用tuple()转换为元组
    元组不可被修改,可以作为字典的key
'''
c = {2: 1, 3: 2, 4: 3, 5: 4}  # 字典
'''
    形式: { "key" : "value" }
    key可以是字符,可以是数字,value也如此
    使用dict()转换为字典
    作为key的是永远都是不可被修改量
    
'''
d = {1, 1, 3, 4, 5}  # 集合
'''
    一样的数据只会包含一次
    集合内部的元素要为不可更改的类型
    
    集合会自动排序
'''

x = string.ascii_letters
listA = [random.choice(x) for i in range(1000)]
dictA = dict()
for a in listA:
    dictA[a] = dictA.get(a, 0) + 1
print([f'{i}->{dictA[i]}' for i in list(x)])










