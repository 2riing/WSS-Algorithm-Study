import sys
sys.stdin = open('../0420/input.txt')

# 1과 자신의 수 말고는 나눌 수 없음
# 예를 들면 n이라는 숫자가 있으면 1, n 제외의 숫자 외에는 나눌 수가 없다.

N = int(input())
numbers = list(map(int, input().split()))
result = []

for number in numbers:
    for i in range(2 , number // 2 + 1):
        if number % i == 0: # 정확하게 나눠 떨어지면?
            result.append(number)
            break

total = len(set(numbers) - set(result)) # 차집합 사용
if 1 in numbers:
    total -= 1
    print(total)
else:
    print(total)


