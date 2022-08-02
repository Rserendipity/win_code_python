import random
import os

'''      作业1     '''
# 创建列表
aList = [random.randint(1, 100) for x in range(10)]
print("创建列表:" + str(aList))

# 原地升序排列
aList.sort()
print("原地升序排列:" + str(aList))

# 删除最后一个元素
aList.pop(-1)
print("删除最后一个元素:" + str(aList))

# 把第零个元素移动到尾部
aList.append(aList[0])
del aList[0]
print("把第零个元素移动到尾部:" + str(aList))

# 在第三个位置上插入数值99
aList.insert(2, 99)
print("在第三个位置上插入数值99:" + str(aList))

# 返回新列表
new = aList[::]
print("原列表地址:" + str(id(new)))
print("新列表地址:" + str(id(aList)))

# 返回奇数与偶数列表
L1 = aList[0::2]
L2 = aList[1::2]
print("奇数序列:" + str(L1))
print("偶数序列:" + str(L2))

# 合并
L3 = list(zip(L1, L2))
print('合并后:' + str(L3))

'''    作业2      '''
# 列出1900年以来所有的闰年
listYear = [x for x in range(1900, 2022) if (x % 400 == 0) or (x % 100 != 0 and x % 4 == 0)]
print('列出1900年以来所有的闰年:' + str(listYear))

'''    作业3     '''
# 列出c:\windows下所有exe和dll文件
listFile = [x for x in os.listdir(r'c:\Windows')]  # 获取文件信息

newListFile = [listFile[i] for i in range(1, len(listFile)) if str(listFile[i]).endswith(('.exe', '.dll'))]  # 使用列表推导
print(newListFile)

for i in range(1, len(listFile)):  # 使用传统for循环
    if str(listFile[i]).endswith(('.exe', '.dll')):
        print(listFile[i])
