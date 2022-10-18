n = 0
result = []
for i in range(1, 10001):
    result.append(i)
for j in range(1, 10001):
    a = b = c = d = 0
    if j < 10:
        n = j + j
        if n not in result:
            pass
        else:
            result.remove(n)
    elif j < 100:
        c = j // 10
        d = j % 10
        n = j + c + d
        if n not in result:
            pass
        else: result.remove(n)
    elif j < 1000:
        b = j // 100
        c = (j // 10) % 10
        d = j % 10
        n = j+b+c+d
        if n not in result:
            pass
        else: result.remove(n)
    elif j < 10000:
        a = j // 1000
        b = (j // 100) % 10
        c = (j // 10) % 10
        d = j % 10
        n = j+a+b+c+d
        if n not in result:
            pass
        else:
            result.remove(n)

print(*result, sep='\n')

# 6  3+ 3