d = [list(map(int, input().split())) for _ in range(10)]


x, y = 1, 1

while True:

    d[1][1] = 9

    if d[x][y + 1] == 0:
        d[x][y + 1] = 9
        y += 1

    if d[x][y + 1] == 1:
        x += 1
        if d[x][y] == 1:
            break
        elif d[x][y] == 0:
            d[x][y] = 9
        else:
            d[x][y] = 9
            break

    if d[x][y + 1] == 2:
        d[x][y + 1] = 9
        break

for i in range(10):
    for j in range(10):
        print(d[i][j], end=" ")
    print()
