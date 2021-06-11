h, w = map(int, input().split())  # 가로, 세로 길이

list = [[0 for i in range(w + 1)] for j in range(h + 1)]  # 2차원 list 만들기

n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 1:
            list[x + j][y] = 1
        else:
            list[x][y + j] = 1


# 결과 출력
for i in range(1, h + 1):
    for j in range(1, w + 1):
        print(list[i][j], end=" ")
    print()
