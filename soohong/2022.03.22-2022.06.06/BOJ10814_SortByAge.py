import sys
sys.stdin = open('../0511/input.txt')

N = int(input())
people = [[] for _ in range(N)] # 빈 배열 생성
for i in range(N):
    a, b = input().split()
    people[i].append(int(a)) # 정렬을 위해서 int로 넣어줌
    people[i].append(b)

# 정렬
people.sort(key=lambda x:x[0])

for i in range(N):
    print(*people[i])