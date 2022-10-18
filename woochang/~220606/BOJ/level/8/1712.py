A, B, C = map(int, input().split())
son = -1
while True:
    x = 1
    g = A + B*x
    b = C * x
    if g < b:
        son = x
        break
    else: x += 1
print(son)
