import heapq

def solve():
    n = 3
    l = [8, 5, 8]

    h = []

    for i in l:
        heapq.heappush(h, i)

    ans = 0

    while(len(h) > 1):
        min = heapq.heappop(h)
        second_min = heapq.heappop(h)
        s = sum([min, second_min])
        ans += s
        heapq.heappush(h, s)

    print(ans)

solve()