import pymysql

if __name__ == '__main__':
    filename = ['ch0.txt', 'ch1.txt', 'ch2.txt', 'ch3.txt',
                'en0.txt', 'en1.txt', 'en2.txt', 'en3.txt', ]
    fileio = []
    for name in filename:
        # print(name)
        fileio.append(open(name, 'r'))

    print('open file success!')

    try:
        db = pymysql.connect()
    except:
        print('connect fail')
        for io in fileio:
            io.close()
        exit(-1)

    cursor = db.cursor()

    sql = 'insert into word values(null, %s, %s, %s, %s, %s, %s, %s, %s);'

    for i in range(4449):
        words = []
        for io in fileio:
            words.append(io.readline())
        cursor.execute(sql, words)
        print(f'已经插入{i}条数据')

    db.commit()
    print('提交完成')

    # print(sql)

    #  cursor.execute(sql)
