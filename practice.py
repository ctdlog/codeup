d = [list(map(int, input().split())) for _ in range(19)]

n = int(input())
for i in range(n):
    x, y = input().split()
    for j in range(19):
        if d[j][int(y)] == 0:
            d[j][int(y)] = 1
        else:
            d[j][int(y)] = 0

        if d[int(x)][j] == 0:
            d[int(x)][j] = 1
        else:
            d[int(x)][j] = 0

for i in range(19):
    for j in range(19):
        print(d[i][j], end=" ")  # 공백을 두고 한 줄로 출력
    print()  # 줄 바꿈
