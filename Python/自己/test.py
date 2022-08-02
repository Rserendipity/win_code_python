scores = [94, 89, 96, 88, 92, 86, 69, 95, 78, 85]

# 1.平均值
print("平均值:", sum(scores)/len(scores))


# 2.最高的三个成绩和最低的三个成绩
newScores = scores[::]  # 拷贝一份列表
newScores.sort()  # 把新列表升序排列一遍
print("三个成绩最低的:", end="")
for i in range(0, 3, 1):  # 输出三个成绩最低的
    print(newScores[i], end=" ")
print("\n三个成绩最高的:", end="")
for i in range(1, 4, 1):  # 输出三个成绩最高的
    print(newScores[-i], end=" ")


# 3.成绩中位数
newScores = scores[::]  # 拷贝一份列表
newScores.sort()  # 把新列表升序排列一遍
del newScores[0]  # 删除最低成绩最高成绩
del newScores[-1]
print("\n中位数:", sum(newScores)/len(newScores))


# 4.最高分和最低分
print("max =", max(scores))
print("min =", min(scores))


# 5.成绩分段存储
more90 = open("more90.txt", "w")  # 以w(write的缩写)的形式打开文件"more90.txt"
more80 = open("more80.txt", "w")  # 如果文件不存在,会创建一个新的文件
more70 = open("more70.txt", "w")  # 如果文件存在,会把文件内容删除

newScores = scores[::]  # 拷贝一份列表
newScores.sort()  # 把新列表升序排列一遍

'''  传统方法
for i in newScores:
    if 70 <= i < 80:
        more70.write(str(i) + " ")
for i in newScores:
    if 80 <= i < 90:
        more80.write(str(i) + " ")
for i in newScores:
    if 90 <= i < 100:
        more90.write(str(i) + " ")
'''

'''  列表推导式  '''
[more70.write(str(i) + " ") for i in newScores if 70 <= i < 80]
[more80.write(str(i) + " ") for i in newScores if 80 <= i < 90]
[more90.write(str(i) + " ") for i in newScores if 90 <= i < 100]

more70.close()  # 关闭文件,释放文件资源,也确保写入
more80.close()
more90.close()
