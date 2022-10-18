a, b = map(int, input().split()) 
if a >= 0 and b >= 45:
    print(int(a), int(b-45))
elif a == 0 and b < 45:
    print(23, int(b+15))

else:
    print(int(a-1), int(b+15))