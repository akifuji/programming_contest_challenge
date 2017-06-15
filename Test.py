n, k = map(int, input().split())
s = input()

bag = []
def solve(i, r, s):
    if i == n:
        bag.append(s)
        print(s)
    else:
        if s[i] == '0':
            if r+1 < k:
                solve(i+1, r+1, s)
        elif s[i] == '?':
            if r+1 < k:
                solve(i+1, r+1, s[:i] + '0' + s[i+1:])
            solve(i+1, 0, s[:i] + '1' + s[i+1:])
        else:
            solve(i+1, 0, s)

solve(0, 0, s)

if len(bag) == 0:
    print("None")
