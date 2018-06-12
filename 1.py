# 1(a)
def f_1a(s):
    return s[::-1]

# 1(b)
def f_1b(s):
    output = ''
    l = s.split(' ')
    for i in range(len(l)):
        l[i] = l[i][::-1]
    return " ".join(l)