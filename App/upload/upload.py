#
# 上传用户的信息
#

def upload(sql, user_info):
    s = "update user_info set "
    s += "user_password = '"
    s += user_info[2] + "'"
    s += ",user_current_save = "
    s += str(user_info[3])
    s += ",user_everyday_num = "
    s += str(user_info[4])
    s += ",user_pause_way = "
    if user_info[5]:
        s += "1"
    else:
        s += "0"
    s += " where user_name like '"
    s += user_info[1]
    s += "';"
    sql.execute(s)


#     update
#     user_info
#     set
#     user_current_save = 25,
#     user_everyday_num = 3,
#     user_pause_way = false
#     where
#     user_name
#     like
#     'cjj';

