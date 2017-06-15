def partialSum(a, n, k, i, s):
    if i == n:
        return k == s
    if partialSum(a, n, k, i+1, s+a[i]):
        return True
    if partialSum(a, n, k, i+1, s):
        return True
    return False

def solve(a, n, k):
    print(partialSum(a, n, k, 0, 0))

n = 4
a = [1, 2 ,4, 7]
k = 13

solve(a, n, k)