from user.register import user_register
from util import mydb

db = mydb.mydb()

while True:
    user_info = user_register(db)
    if user_info:
        print('your info:')
        for k, v in user_info.items():
            print(f'{k} is {v}')
        break
    else:
        print('you want to register username has been registered')

# user_info = {'id':1}
#
# for k,v in user_info.items():
#     print(k, v)
