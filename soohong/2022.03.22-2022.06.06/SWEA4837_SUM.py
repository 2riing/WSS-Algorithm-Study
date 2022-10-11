import sys
sys.stdin = open('input.txt')
from itertools import combinations

#기본 입력
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 조합을 통해서 picks에 경우의 수 모두 만들어주기
    picks = list(combinations(range(1,13),N))
    cnt = 0
    for pick in picks:
        if sum(pick) == K: # 합이 K와 같으면
            cnt += 1
    print(f'#{tc} {cnt}')