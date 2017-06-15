def antsMin(L, n, x):
    for i in range(n):
        if x[i] > L - x[i]:
            x[i] = L - x[i]
    print(max(x))

def antsMax(L, n, x):
    for i in range(n):
        if x[i] < L - x[i]:
            x[i] = L - x[i]
    print(max(x))

L = 10
n = 3
x = [2, 6, 7]

antsMin(L, n, x)
antsMax(L, n, x)
