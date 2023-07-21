from user.login import user_login
from util import mydb

db = mydb.cjjdb()

user_info = user_login(db)
if user_info:
    print('your info:')
    for k, v in user_info.items():
        print(f'{k} --> {v} --> {type(v)}')
else:
    print('dont have this user')

# user_info = {'id':1}
#
# for k,v in user_info.items():
#     print(k, v)
