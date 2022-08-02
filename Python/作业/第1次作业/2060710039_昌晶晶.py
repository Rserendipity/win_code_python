"""  1 """
print("Hello World")

'''  2  '''
num1 = 100 + 200
num2 = 123 - 234
num3 = 345 * 13
num4 = 123 / 23
num5 = 233 // 323
print(f"{num1} {num2} {num3} {num4} {num5}")

'''  3   '''
# 下载命令   pip install progressbar
# 熟悉了ubuntu的下载命令，容易敲错... apt install XXX

'''  4   '''
i = 1
myString = "I like python "
print("The output is :", end="")
# while循环
while i < 30:
    print(myString, end="")
    i += 1
# format函数
print("\n", "The output is {}".format(myString))

'''  5   '''
string1 = "Hello "
string2 = "World"
# 字符串拼接
print(string1 + string2)
# f"{}" 打开
print(f"{string1}{string2}")

