import sys
sys.stdin = open('1859input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    total = 0
    max_num = arr[N - 1] # 맨 끝값을 최댓값으로 일단 설정
    
    for i in range(N - 1, 0, -1):
        # 맨뒤 시작이라 N-1 # i-1값과 비교하기때문에 -1이 아니라 0
        if  max_num < arr[i - 1]:
            #최댓값으로 지정한 값보다 앞의 값이 크면 total 변동없이 바꿔줌
            max_num = arr[i - 1]

        else:
            total += (max_num - arr[i - 1])
            # 차이만큼 더하는것이기때문에 최댓값-이전값
    print(f'#{tc} {total}')