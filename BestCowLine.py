# coding=utf-8

def best_cow_line(s):
    t = []
    while s:
        if s <= s[::-1]:
            t.append(s[0])
            s = s[1:]
        else:
            t.append(s[-1])
            s = s[:-1]
    print(t)


s = "ACDBCB"
best_cow_line(s)