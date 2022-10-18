# A, B = map(str, input().split())
# a, b = 'abc', 'def'
# for i in range(3):
#     a[i] = A[2-i]
#     b[i] = B[2-i]
# c = int(a)
# d = int(b)
# if c>d:
#     print(c)
# else: print(d)
A, B = map(int, input().split())
a = (A // 100) + ((A // 10)%10)*10 + (A%10)*100
b = (B // 100) + ((B// 10)%10)*10 + (B%10)*100
if a>b:
    print(a)
else: print(b)
