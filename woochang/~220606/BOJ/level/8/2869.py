A, B ,V = map(int,input().split())
cnt = 1
# x = 0
# while True:
#     x += A
#     if x > V:
#         print(cnt)
#         break
#     else:
#         x -= B
#         cnt += 1
print((V-A) // (A-B)  + 1)
