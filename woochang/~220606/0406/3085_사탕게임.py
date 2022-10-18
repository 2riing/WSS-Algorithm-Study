import sys
sys.stdin=open('3085input.txt')

N = int(input())
arr = [list(map(str, input())) for _ in range(N)]
print(arr)


# 1. 완탐 해서 2칸 바꾼거를 행, 열 최댓값 계산
# 2. 최댓값 계산하는것도 조건 까다로움
# 3.박스에 C,P,Z,Y 넣고 인덱스 값이나 수량으로 더해줘야될듯