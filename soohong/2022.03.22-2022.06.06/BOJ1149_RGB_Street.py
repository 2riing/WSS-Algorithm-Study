import sys
sys.stdin = open('../0504/input.txt')

N = int(input()) # 전체 집의 개수
RGBs = [list(map(int, input().split())) for _ in range(N)]


ans = []
for s_num in range(N):
    result = 0
    for i in range(N):
        if s_num + i > N - 1:
            h_num = s_num + i - (N - 1)
        else:
            h_num = i + s_num
        min_num = 1000
        min_idx = 0
        for idx in range(3):
            if RGBs[h_num][idx] < min_num:
                min_num = RGBs[h_num][idx]
                min_idx = idx
        result += min_num
        if h_num+1 < N:
            RGBs[h_num+1][min_idx] = 1000 # 다음집의 같은 RGB 값 막아주기
    ans.append(result)


print(ans)
