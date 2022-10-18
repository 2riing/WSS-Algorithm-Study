# T = int(input())
# a = int(input())
# b = int(input())
# for i in T:
#     i = a + b
#     print(i)

t = int(input())

for _ in range(t):
  a,b = map(int, input().split())
  print(a+b)