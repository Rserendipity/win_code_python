import pymysql
from log import user_loging
from os import system
from word import word
from memorize_words import memorize_words
from upload import upload

# 设置命令行的字符集
system('chcp 65001')
system('cls')

# 连接数据库
connect = pymysql.connect(host='1.15.113.185',
                          port=3306,
                          user='cjj',
                          password='Cjj020427@',
                          database='cjj')
if not connect.open:
    print('无法连接到数据库，请检查网络')
    system('pause')
    exit(-1)
sql = connect.cursor()  # 得到sql句柄

# 登录，成功才会返回，返回的是用户的信息
user_info = user_loging.longin(sql)

# 通过用户信息，例如记录在哪里，今天背多少等，加载单词数据
word_info = word.loading(sql, user_info)

# 用户背单词
memorize_words.choose_chinese(word_info, user_info[5])
memorize_words.choose_english(word_info, user_info[5])
print('恭喜你已完成今日的任务！')

# 上传记录
upload.upload(sql, user_info)

system('pause')
