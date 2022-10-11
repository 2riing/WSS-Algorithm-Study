import sys
sys.stdin = open('../0504/input.txt')


# 먼저 첫번째와 두번째를 비교해서
# 1 < 2 어센딩
# 1 > 2 디센딩
# 그 이후값이 어센딩 or 디센딩 조건 만족못하면 믹스드

numbers = list(map(int, input().split()))

def find_scale():
    N = len(numbers)
    scale = ['ascending',
             'descending',
             'mixed']
    result = ''
    if numbers[0] < numbers[1]: # ascending
        result = scale[0]
    elif numbers[0] > numbers[1]: # descending
        result = scale[1]
    else:
        result = scale[2]
        return result

    for i in range(1, N-1):
        if result == scale[0] and numbers[i] < numbers[i+1]:
            pass
        elif result == scale[1] and numbers[i] > numbers[i+1]:
            pass
        else:
            result = scale[2]
            return result
    return result

print(find_scale())








