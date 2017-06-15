field = [
    ['W', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['.', 'W', 'W', 'W', '.', '.', '.', '.', '.', 'W', 'W', 'W'],
    ['.', '.', '.', '.', 'W', 'W', '.', '.', '.', 'W', 'W', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
    ['.', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
    ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['W', '.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', '.'],
    ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.'],
    ['.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', 'W', '.'],
    ]

def lake_counting(n, m):
    count = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == "W":
                count += 1
                is_face_water(n, m, i, j)
    print(count)

def is_face_water(n, m, i, j):
    field[i][j] = "."
    for x in range(-1, 2):
        for y in range(-1, 2):
            nx = i + x
            ny = j + y
            if (nx >= 0 and nx < n and ny >= 0 and ny < m and\
                field[nx][ny] == "W"):
                is_face_water(n, m, nx, ny)

print(lake_counting(len(field), len(field[0])))
