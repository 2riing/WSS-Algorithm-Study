import sys
sys.stdin = open('input.txt')


def Hanoi(pan):
    if pan % 2 == 0:  # 짝수
        pass
    else:  # 홀수
        pass

N = list(range(1, int(input())+1)) # 옮길 숫자들을 배열로 받아옴
tower = [[] for _ in range(max(N))]
tower[0] = N
print(tower)

Hanoi(1)



print(2**max(N) -1)