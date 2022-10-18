T = int(input())

for tc in range(1,T+1):
    P, Q, R, S, W = map(int, input().split())
    asa = P*W
    bsa = 0
    if R > W :
        bsa = Q
    else:
        bsa = Q + S*(W-R)
    ans = min(asa,bsa)
    print(f'#{tc} {ans}')