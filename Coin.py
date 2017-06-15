
def coin(c, A):
    V = [1, 5, 10, 50, 100, 500]
    count = 0

    for i in range(len(V)-1, -1, -1):
        t = min(A // V[i], c[i])
        A -= V[i] * t
        count += t

    return count

c = [3, 2, 1, 3, 0, 2]
print(coin(c, 620))
