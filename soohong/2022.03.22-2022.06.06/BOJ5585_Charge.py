import sys
sys.stdin = open('input.txt')

coins = [500, 100, 50, 10, 5, 1]

N = int(input())

temp = 1000- N
cnt = 0
for coin in coins:
    if temp // coin > 0: # 해당 코인보다 크면
        cnt += temp // coin # 몫은 더해주고
        temp = temp % coin # 나머지로 갱신해줌
    else:
        pass
print(cnt)