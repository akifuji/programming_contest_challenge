import math

n = int(input())
a = [0 for i in range(n)]

s = input().split()

for i in range(n):
    a[i] = int(s[i])

sum = sum(a)
half_sum = math.ceil(sum / 2)

a.sort(reverse=True)

def calculate(i, c):
    if c == 0 or i >= n-1:
        ans = int(half_sum + c)
        print(max(ans, sum-ans))
    else:
        while a[i] > c:
            i += 1
            if i >= n-1:
                break
        c -= a[i]
        i += 1
        calculate(i, c)

calculate(0, half_sum)