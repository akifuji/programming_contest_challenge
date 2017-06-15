def schedule(n, s, t):

    works = [[0 for i in range(2)] for j in range(n)]

    for i in range(n):
        works[i][0], works[i][1] = s[i], t[i]

    sorted(works, key=lambda x:x[1])

    current = 0
    count = 0

    for work in works:
        if current < work[0]:
            count += 1
            current = work[1]

    return count

n = 5
s = [1, 2, 4, 6, 8]
t = [3, 5, 7, 9, 10]

print(schedule(n, s, t))