import pymysql

from util import mydb

# db = pymysql.connect(host='1.15.113.185', user='cjj', password='Cjj020427@', database='cjj', port=3306)
#
# cur = db.cursor()
#
# sql = "update users set " \
#       "user_passwd = %s, current_plan = %s, goal_plan = %s, is_pause = %s" \
#       " where user_name = %s"
# user_info = ['xxx',
#              5,
#              123,
#              False,
#              '123']
#
# cur.execute(sql, user_info)
# db.commit()

# user_name = str(123)
# sql = 'select * from users where user_name = %s'
# cur.execute(sql, [user_name])
# ret = cur.fetchone()
# if ret is not None:
#     print(list(ret))
# else:
#     print([])

db = mydb.cjjdb()
user_info = db.get_userinfo([123, 123])

for k,v in user_info.items():
    print(f'{k} {v}')

db.update_plan(user_info)

# words = db.get_words(1, 3)
#
# for word in words:
#     print(word)
