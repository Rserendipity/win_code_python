from util import mydb


def user_login(db: mydb) -> dict:
    user_name = input('input your user_name:>')
    user_passwd = input('input your user_password:>')
    return db.get_userinfo([user_name, user_passwd])
