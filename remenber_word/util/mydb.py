import pymysql


class cjjdb:
    def __init__(self):
        try:
            self.db = pymysql.connect(host='localhost', user='root', password='123456', database='member_words', port=3306)
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
        sql = "INSERT INTO users VALUES (null, %s, %s, 1, 5, true)"

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

    # 更新用户进度
    def update_plan(self, user_info: dict):
        sql = "UPDATE users SET " \
              "current_plan = %s " \
              "WHERE user_name = %s"

        update_info = [user_info['current_plan'] + user_info['goal_plan'], user_info['user_name']]
        self.cursor.execute(sql, update_info)
        self.db.commit()


    # 获取单词列表 从单词id开始, 获取size个单词数据 查询失败返回空
    def get_words(self, begin_id: int, size: int) -> list:
        sql = 'SELECT ch0, en0, en1, en2, en3  FROM word LIMIT %s OFFSET %s'
        self.cursor.execute(sql, [size, begin_id - 1])
        word = self.cursor.fetchall()
        if word:
            return list(word)
        else:
            return []
