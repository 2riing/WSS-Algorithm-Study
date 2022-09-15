numbers = [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
hand =["right","left","right"]

def solution(numbers, hand):
    answer = ''
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 11
    L_position = 10
    R_position = 12
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            L_position = i
        elif i in [3, 6, 9]:
            answer += 'R'
            R_position = i
        else:
            l = L_position // 3
            if R_position % 3 == 0:
                r = (R_position - 2) // 3
            else:
                r = R_position // 3
            c = i // 3

            l_d = abs(c-l)+1
            r_d = abs(c-r)+1
            if L_position in [2,5,8,11]:
                l_d = abs(c-l)
            if R_position in [2, 5, 8, 11]:
                r_d = abs(c - r)

            if l_d<r_d:
                answer += 'L'
                L_position = i
            elif l_d>r_d:
                answer += 'R'
                R_position = i
            elif l_d == r_d:
                if hand == 'right':
                    answer += 'R'
                    R_position = i
                else:
                    answer += 'L'
                    L_position = i

    return answer


for i in range(len(numbers)):
    solution(numbers[i], hand[i])