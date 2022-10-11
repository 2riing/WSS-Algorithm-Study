import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))


    max_price = max(prices)

    cnt = 0
    for price in prices:
        if price == max_price:
            break
        else:
            cnt += 1
    print(cnt*max_price)

