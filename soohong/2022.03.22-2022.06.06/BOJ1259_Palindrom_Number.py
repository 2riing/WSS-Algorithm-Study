import sys
sys.stdin = open('../0511/input.txt')

# 거꾸로 해도 이효리 0, -1 / 1, -2 / 2
def isPalindrom(number):
    N = len(number)
    visited = [0 * N]  # 0,0,0,0,0
    start, end = 0, -1
    for _ in range(int(N / 2)):
        if number[start] != number[end]:
            return 0
        else:
            start += 1
            end -= 1
    return 1

while True:
    number = input()
    if number == '0':
        break
    else:
        if isPalindrom(number):
            print('yes')
        else:
            print('no')





