def triangle(n, a):
    ans = 0
    for i in range(n):
        for ii in range(i+1, n):
            for iii in range(ii+1, n):
                s = sum([a[i], a[ii], a[iii]])
                ma = max(a[i], a[ii], a[iii])
                rest = s - ma
                if rest > ma:
                    ans = max(s, ans)
    print(ans)

n = 5
a = [2, 3, 4, 5, 10]

triangle(n, a)
