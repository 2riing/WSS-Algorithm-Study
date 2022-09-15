# 왼손과 오른손의 엄지손가락을 이용해서 숫자 입력
# 왼손은 * 오른손은 #에서 시작
# 147 왼손 369오른손 2580양손중에 가까운, 거리가 같다면 각자 주 손으로 사용
# 어떤 손으로 눌렀는지 반환
# 거리를 어떻게 구해주는지가 문제의 핵심..\
def solution(numbers, hand):
    keypad = [(3,1), (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2, 0), (2,1), (2, 2)]
    left, right = (3,0), (3,2)
    answer = ''    
    for number in numbers:
        if number in [1,4,7]:
            left = keypad[number]
            answer += 'L'
        elif number in [3,6,9]:
            right = keypad[number]
            answer += 'R'
        elif number in [2,5,8,0]: # 가운데에 있을 경우
            cur = keypad[number]
            # 거리를 계산한다
            Ldist = abs(cur[0]-left[0])  + abs(cur[1]-left[1]) 
            Rdist = abs(cur[0]-right[0]) + abs(cur[1]-right[1]) 
            if Rdist < Ldist:
                right = cur
                answer += 'R'
            elif Ldist < Rdist:
                left = cur
                answer += 'L'
            else: # 거리가 같으면
                if hand == 'right':
                    right = cur
                    answer += 'R'
                elif hand == 'left':
                    left = cur
                    answer += 'L'
    return answer