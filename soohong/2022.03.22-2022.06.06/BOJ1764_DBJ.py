import sys
sys.stdin = open('../0511/input.txt')

# 기본입력
N, M = map(int, input().split())

# 듣보들 set으로 입력
never_seen = set(input() for _ in range(N))
never_heard = set(input() for _ in range(M))

# 교집합 구해서 results에 넣어줌
results = sorted(list(never_seen & never_heard))

# 출력
print(len(results))
for result in results:
    print(result)


