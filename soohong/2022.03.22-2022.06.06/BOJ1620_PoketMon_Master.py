#


import sys
sys.stdin = open('../0511/input.txt')

# basic input
N, M = map(int, input().split())

Poket_book = {}
reverse_Poket_book = {}

# make Poket_book & reverse Poket_book / key : number / value : poketmon_name
for number in range(1, N+1):
    PoketMon = sys.stdin.readline().strip()
    Poket_book[number] = PoketMon
    reverse_Poket_book[PoketMon] = number

# solve the Quest
for _ in range(M):
    question = sys.stdin.readline().strip()
    # isnumber(key)
    if question.isdigit():
        print(Poket_book[int(question)])
    # is char(value)
    else:
        print(reverse_Poket_book[question])

