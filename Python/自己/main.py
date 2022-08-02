score = [['Angle', '0121701100106', 99],
         ['Jack', '0121701100107', 86],
         ['Tom', '0121701100109', 77],
         ['Smith', '0121701100111', 100],
         ['Bob', '0121701100115', 77],
         ['Lily', '0121701100117', 59]]


def sort_by_name(aa):
    return sorted(aa, key=lambda x: x[0])


def sort_by_id(aa):
    return sorted(aa, key=lambda x: x[1])


def sort_by_score(aa):
    return sorted(aa, key=lambda x: (x[2], x[0]))


if __name__ == '__main__':
    print('按姓名排序后的结果：', sort_by_name(score))
    print('按学号排序后的结果：', sort_by_id(score))
    print('按成绩排序后的结果：', sort_by_score(score))
