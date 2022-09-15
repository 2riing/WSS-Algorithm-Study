def find_index(n):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == n:
                return (i, j)


def solution(numbers, hand):
    answer = ''
    left = (3, 0)
    right = (3, 2)
    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            left = find_index(number)
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            right = find_index(number)
        elif number == 2 or number == 5 or number == 8 or number == 0:
            # 번호의 인덱스
            key = find_index(number)
            # 왼손/오른손~번호까지의 거리
            l_d = abs(key[0] - left[0]) + abs(key[1] - left[1])
            r_d = abs(key[0] - right[0]) + abs(key[1] - right[1])
            if l_d == r_d:
                if hand == 'left':
                    answer += 'L'
                    left = key
                else:
                    answer += 'R'
                    right = key
            elif l_d < r_d:
                answer += 'L'
                left = key
            elif l_d > r_d:
                answer += 'R'
                right = key
    return answer