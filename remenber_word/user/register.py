from util import mydb


def user_register(db: mydb) -> dict:
    user_name = input('input your user_name:>')
    user_passwd = input('input your user_password:>')
    if db.add_user([user_name, user_passwd]):
        return db.get_userinfo([user_name, user_passwd])
    else:
        return {}
