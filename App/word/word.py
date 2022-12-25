def loading(sql, user_info):
    s = 'select en_current,en_err1,en_err2,en_err3,ch_current,ch_err1,ch_err2,ch_err3' \
        ' from word where id >= '\
        + str(user_info[3] + 1) \
        + ' and id <= ' \
        + str(user_info[3] + user_info[4]) \
        + ';'
    sql.execute(s)
    return sql.fetchall()


# select * from word where id >= 1 and id <= 10;
