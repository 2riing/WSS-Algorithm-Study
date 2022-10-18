import sys
sys.stdin = open('4831input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split())) +[N]
    # print(arr)
    cnt = M
    for i in range(M):
        if arr[i+2] - arr[i] <=K:
            cnt -= 1
    for i in range(M+1):
        if arr[i+1] - arr[i] > K:
            cnt = 0
            break
    print(f'#{tc} {cnt}')




    # # print(K)
    # # print(N)
    # # print(arr)
    # stop = [0]*(N+K)
    # for i in arr:
    #     stop[i] = 1
    # # print(stop)
    # cnt = 0
    # for i in range(N):
    #     for j in range(K,0,-1):
    #         if stop[i+j] == 1:
    #             cnt += 1
    #             i += j
    #         else:
    #             break
    #     break
    # print(f'#{tc} {cnt}')







    #조건
# for문 돌려서 정류장 번호랑 다르면 패스
# 현재위치+K값보다 정류장 번호가 높으면 패스
# 현재위치+k값보다 정류장 번호가 낮은거 중에 최댓값 (거꾸로 돌리기)
#
# 1. 노선수 T , 1회 최대 이동 가능거리 K, 정류장 개수 N, 충전소 설치 개수 M
# 2. M값은 밑에 split 형태로 주어짐

