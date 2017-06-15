field = [
    ['#', 'S', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '#'],
    ['.', '#', '.', '#', '#', '.', '#', '#', '.', '#'],
    ['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
    ['.', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '.', '#', '#', '#', '.'],
    ['.', '.', '.', '.', '#', '.', '.', '.', 'G', '#'],
    ]

def maze(sx, sy, gx, gy, field):
    x_length = len(field)
    y_length = len(field[0])

    INF = 100000000
    distance = [[INF for i in range(x_length)] for j in range(y_length)]

    queue = []
    queue.insert(0, (sx, sy))
    distance[sx][sy] = 0

    while len(queue):
        x, y = queue.pop()

        if x == gx and y == gy:
            print(distance[gx][gy])

        for i in range(0, 4):
            nx, ny = [-1, 0, 1, 0][i] + x, [0, -1, 0, 1][i] + y
            if (nx >= 0 and nx < x_length and ny >= 0 and ny < y_length\
                 and field[nx][ny] != "#" and distance[nx][ny] == INF):
                queue.insert(0, [nx, ny])
                distance[nx][ny] = distance[x][y] + 1

sx, sy = 0, 1
gx, gy = 9, 8

print(maze(sx, sy, gx, gy, field))
