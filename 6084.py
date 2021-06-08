h, b, c, s = map(int, input().split())
r = h * b * c * s / 8 / 1024 / 1024
print(str(round(r, 1)) + " MB")
