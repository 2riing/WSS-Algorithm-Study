import sys
sys.stdin= open('input.txt')


def fre():
    num = list(set(arr))
    num.sort()
    cnt = [0] * len(num)

    for a in arr:
        for n in range(len(num)):
            if a == num[n]:
                cnt[n] += 1

    max_cnt = max(cnt)
    index_cnt = 1
    if cnt.count(max_cnt) > 1:  # 여러개면
        for i in range(len(cnt)):
            if index_cnt == 2:
                print(num[i])
                return
            elif cnt[i] == max_cnt:
                index_cnt += 1
            else:
                pass
    else:
        for i in range(len(cnt)):
            if cnt[i] == max_cnt:
                print(num[i])
                return


N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
# 산술평균
print(int(round(sum(arr)/N,0)))

# 중앙값 n//2 번째 값
arr.sort()
print(arr[N//2])

# 최빈값
fre()

# 범위
print(max(arr)- min(arr))