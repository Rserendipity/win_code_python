import pymysql
from log import user_loging
from os import system
from word import word
from memorize_words import memorize_words
from upload import upload


def user_set(user_info):
    while True:
        print('你的信息如下\n')
        print('账号：' + user_info[1], end='\t')
        print('密码：' + user_info[2])
        print('总记录：' + str(user_info[3]), end='\t')
        print('每次背诵多少个：' + str(user_info[4]))
        print('当前单词正确时是否暂停：', end='')
        if user_info[5]:
            print('暂停')
        else:
            print('不暂停')

        print('\n1、更改密码')
        print('2、每次背诵个数')
        print('3、背完单词后是否暂停')
        print('4、确认退出')

        user_in = input('\n请选择：')
        if user_in == '1':
            while True:
                new_pass = input('请输入新密码：')
                if new_pass.find("'") != -1:
                    print('含有非法字符！')
                else:
                    user_info[2] = new_pass
                    break

        elif user_in == '2':
            while True:
                new_size = input('请输入新个数：')
                if not str(new_size).isdigit():
                    print('含有非法字符！')
                else:
                    user_info[4] = int(new_size)
                    break

        elif user_in == '3':
            print('现在更改为：', end='')
            if not user_info[5]:
                print('暂停')
                user_info[5] = not user_info[5]
            else:
                print('不暂停')
                user_info[5] = not user_info[5]

        elif user_in == '4':
            break
        else:
            print("错误的输入")

        system('pause')
        system('cls')


def user_join(sql, connect):
    while True:
        user_name = input('请输入用户名：')
        if user_name.find("'") != -1:
            print("含有非法字符！")
            continue
        sql.execute("select id from user_info where user_name like '" + user_name + "';")
        result = sql.fetchone()
        if result:
            print('已重复，请重新输入账号名')
            system('pause')
            system('cls')
            continue

        break

    user_info = [0, user_name, '123456', 0, 5, 0]
    s = "insert into user_info values (" + "0,'" + user_name + "',123456,0,5,0);"
    sql.execute(s)
    print('创建中.....')
    connect.commit()
    print('完成.....')
    user_set(user_info)
    print('正在上传你的信息.......')
    upload.upload(sql, user_info)
    connect.commit()
    print('上传完成..........')
    system('pause')
    system('cls')

def menu(sql, connect):
    # 登录，成功才会返回，返回的是用户的信息
    user_info = list(user_loging.longin(sql))
    connect.commit()  # 提交本次的sql语句
    while True:
        print('1、设置')
        print('2、开始背单词')
        print('3、退出\n')
        user_input = input('请选择：')

        if user_input == '1':
            system('cls')
            user_set(user_info)
            print('正在上传你的信息.......')
            upload.upload(sql, user_info)
            connect.commit()
            print('上传完成..........')
            system('pause')
            system('cls')

        elif user_input == '2':
            system('cls')
            # 通过用户信息，例如记录在哪里，今天背多少等，加载单词数据
            word_info = word.loading(sql, user_info)
            connect.commit()
            # 用户背单词
            memorize_words.choose_chinese(word_info, user_info[5])
            memorize_words.choose_english(word_info, user_info[5])
            user_info[3] += user_info[4]
            print('恭喜你已完成本次的背诵！')
            # 上传记录
            print('上传记录中.....')
            upload.upload(sql, user_info)
            connect.commit()
            print('完成......')
            system('pause')
            system('cls')

        elif user_input == '3':
            break

        else:
            print('错误的选择!')
            system('pause')
            system('cls')


if __name__ == '__main__':

    # 设置命令行的字符集
    system('chcp 65001')
    system('cls')
    print('连接中.......')

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

    print('连接成功.......')
    system('pause')
    system('cls')

    while True:
        system('cls')
        print('1、注册')
        print('2、登录')
        print('3、退出\n')

        user_in = input('请选择：')
        if user_in == '1':
            user_join(sql, connect)
        elif user_in == '2':
            # 菜单，登录、修改信息、背单词
            menu(sql, connect)
        elif user_in == '3':
            break
        else:
            print('选择错误！')

    # 关闭连接
    connect.commit()
    connect.close()
