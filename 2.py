# 2
def f_2(l):
    cnt = 0
    for i in l:
        if ((i % 3 != 0) and (i % 5 != 0)) or (i % 15 == 0):
            cnt += 1
    return cnt