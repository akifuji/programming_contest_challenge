def sarumans_army(n, x, r):
    position = x[0]
    count = 0

    for i in range(1, n):
        if position + r < x[i]:
            position = x[i]
            count += 1

    print(count)

n = 6
x = [1, 7, 15, 20, 30, 50]
r = 10
sarumans_army(n, x, r)

