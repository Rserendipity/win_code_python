from user.login import user_login
from util import mydb

db = mydb.mydb()

user_info = user_login(db)
if user_info:
    print('your info:')
    for k, v in user_info.items():
        print(f'{k} is {v}')
else:
    print('dont have this user')

# user_info = {'id':1}
#
# for k,v in user_info.items():
#     print(k, v)
