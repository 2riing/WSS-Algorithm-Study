import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    _ = int(input())
    arr = [0]*101 # 0부터 100까지 카운트 셀 arr
    matrix = list(map(int, input().split()))

    for i in matrix: #arr에 숫자 하나씩 대입
        arr[i] += 1
    max_count = 0
    max_index = 0
    for j in range(len(arr)):
        if arr[j] > max_count:
            max_count = arr[j]
            max_index = j  # 인덱스값만 필요함
    print(f'#{tc} {max_index}')
