import sys
sys.stdin = open('input.txt')

T = int(input())
cnt = 0
for _ in range(T):
    arr = []

    N = input()
    cnt_sum = 1
    for i in range(len(N)-1):
        if N[i] == N[i+1]:
            pass
        else:
            arr.append(N[i])
        if N[i+1] in arr:
            cnt_sum = 0
       
    #     if N[i-1] == N[i]:
    #         pass
    #     if N[i-1] != N[i]:
    #         arr.append(N[i-1])

    #         if N[i] in arr:
    #             # cnt_sum = 0
    #             arr.append('11')
    # if '11' in arr:
    #     cnt_sum = 0
    cnt += cnt_sum
print(cnt)