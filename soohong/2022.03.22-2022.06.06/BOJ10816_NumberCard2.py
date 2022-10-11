import sys
sys.stdin = open('../0518/input.txt')

N = int(sys.stdin.readline()) # 가지고 있는 숫자 카드의 개수
cards = list(map(int, sys.stdin.readline().split())) # 각 숫자 카드에 적혀있는 정수
M = int(sys.stdin.readline()) # 몇개 가지고 있는 숫자카드인지 구해야할수?
bucket = [0 for _ in range(M)]
numbers = list(map(int, sys.stdin.readline().split())) # 구해야할 것들
print(cards)
print(numbers)

for card_idx in range(len(cards)):
    if cards[card_idx] == numbers[num_idx]:
        bucket[num_idx] += 1
print(*bucket)