import sys
sys.stdin = open('../0606/input.txt')

# 기본 입력
n = int(input())
arr = list(map(int, input().split()))

dp = [0] * len(arr) # 빈 배열 만들어주기
dp[0] = arr[0] # 초기 값 설정

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i-1] + arr[i])

    # 전에꺼랑 현재꺼 더한 숫자보다, 현재 arr의 숫자가 더 크다면
    # dp에 새로운 값을 저장

    # 전의 숫자부터 더해온게 크다면 dp[i-1] + arr[i] 값을 저장

print(max(dp))