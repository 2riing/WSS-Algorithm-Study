N = int(input())

t = 0
for i in range(1, N+1):
    if i < 100:
        t += 1
    elif i >= 100:
        a = i // 100
        b = (i % 100) // 10
        c = i % 10
        if a <= b <= c :
            if b-a == c-b:
                t +=1
        elif c <= b <= a :
            if a-b == b-c:
                t +=1

print(t)