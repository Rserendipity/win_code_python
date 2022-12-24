from os import system

# 用户登录
def longin(sql):
    while True:
        user_name = input('输入你的用户名:')
        user_passwd = input('输入你的密码:')

        s = "select * from user_info where user_name like '" + user_name + "' and user_password like '" + user_passwd + "';"
        sql.execute(s)

        user_info = sql.fetchone()
        if user_info:
            print('登录成功')
            system('pause')
            system('cls')
            return user_info
        else:
            print('用户名或密码错误')
            system('pause')
            system('cls')
