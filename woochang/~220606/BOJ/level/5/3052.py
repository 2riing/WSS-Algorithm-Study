import sys
sys.stdin = open('input.txt')


lst = [int(input()) for _ in range(10)]
# print(lst)
new = [0]*10
for i in range(10):
    new[i] = lst[i] % 42

result= []
for i in new:
    if i not in result:
        result.append(i)
print(len(result))