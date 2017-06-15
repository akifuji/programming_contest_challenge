def fence_repair(n, l, ans):
    if n == 1:
        print(ans)
    else:
        sorted(l)
        t = l[0] + l[1]
        l = l[2:]
        l.append(t)
        ans += t
        fence_repair(n-1, l, ans)

n = 3
l = [8, 5, 8]
fence_repair(n, l, 0)