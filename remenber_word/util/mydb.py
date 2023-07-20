import pymysql


class mydb:
    def __init__(self):
        try:
            # self.db = pymysql.connect(host='localhost', user='root', password='123456', database='member_words', port=3306)
            self.db = pymysql.connect(host='1.15.113.185', user='cjj', password='Cjj020427@', database='cjj', port=3306)
            self.cursor = self.db.cursor()
        except pymysql:
            print('未能连接数据库')
            exit(-1)

    # 根据 [user_name, user_passwd] 查询用户信息, 如果用户名不存在, 或者密码不正确 返回 空dick
    def get_userinfo(self, user_info: list) -> dict:
        sql = 'SELECT * FROM users WHERE user_name = %s AND user_passwd = %s'
        self.cursor.execute(sql, user_info)
        ret = self.cursor.fetchone()

        if ret is None:
            return {}
        else:
            user_dict = {'id': ret[0],
                         'user_name': ret[1],
                         'user_passwd': ret[2],
                         'current_plan': ret[3],
                         'goal_plan': ret[4],
                         'is_pause': ret[5]
                         }
            return user_dict

    # 新增用户 user_info格式[user_name, user_passwd]
    def add_user(self, user_info: list) -> bool:
        sql = "INSERT INTO users VALUES (null, %s, %s, 0, 5, false)"

        try:
            self.cursor.execute(sql, user_info)
        except pymysql.err.IntegrityError:
            return False

        self.db.commit()
        return True

    # 更新用户信息 user_info格式[user_changed_passwd, current_plan, goal_plan, is_pause, user_name, user_old_passwd]
    def update_user(self, user_info: list) -> bool:
        sql = "UPDATE users SET " \
              "user_passwd = %s, current_plan = %s, goal_plan = %s, is_pause = %s " \
              "WHERE user_name = %s AND user_passwd = %s"

        rows = self.cursor.execute(sql, user_info)
        self.db.commit()
        return rows != 0

    # 获取单词列表
    def get_words(self, begin: int, size: int) -> list:
        pass  # todo
