fees =[[180, 5000, 10, 600],[120, 0, 60, 591],[1, 461, 1, 10]]
records = [["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"],["00:00 1234 IN"]]



def solution(fees, records):

    basic_minute = fees[0] # 기본 시간
    basic_won = fees[1]    # 기본 요금
    unit_minute = fees[2]  # 단위 시간
    unit_won = fees[3]     # 단위 요금

    records2 = []
    car_num = []
    for record in records: # 시간 처리 작업
        stack = []
        stack.append(int(record[0:2])*60 + int(record[3:5]))
        stack.append(record[6:10])
        if [record[6:10],0,0,0] in car_num:
            pass
        else:
            car_num.append([record[6:10],0,0,0]) # [차번호, 시작시간, 합계시간, 출차했냐]
        if record[-1] == 'N':
            stack.append(1)
        else:
            stack.append(-1)

        records2.append(stack)
    answer = []
    for record in records2:
        if record[2] == 1: # 입차
            for i in car_num:
                if i[0] == record[1]:
                    i[1] = record[0]
                    i[3] = 1  # 입차 표시
                    # i[1].append(record[0]) # 이러면 갱신이 안 되서 바꿔주는걸로
        else:  # 출차
            for i in range(len(car_num)):
                if car_num[i][0] == record[1]:
                    car_num[i][2] += (record[0] - car_num[i][1])
                    car_num[i][3] = -1
                    break
    for car in car_num: # 출차 안한거 23:59 계산
        if car[3] == 1:
            car[2] += 1439 - car[1]
        car[0] = int(car[0]) # 차 번호 int화  = 나중에 오름차순 계산
        car[3] = 0   # 차 숫자값 더해줄거
        if car[2] <= basic_minute:  # 계산작업 시작
            car[3] = basic_won
        else:
            over_time = car[2] - basic_minute  # 기본요금 초과 시간
            over_time_a = over_time / unit_minute
            over_time_b = over_time // unit_minute
            if over_time_b-over_time_a < 0:
                over_time_b += 1
            car[3] = (unit_won * over_time_b) + basic_won

    for i in range(len(car_num)): # 차 돌리기
        min_num = [10000,0]
        for j in range(len(car_num)): # 오름차순으로 차 번호 작은거에 값 넣어주기
            if car_num[j][0] < min_num[0]:
                min_num[0] = car_num[j][0]
                min_num[1] = j
        answer.append(car_num[min_num[1]][3])
        car_num[min_num[1]][0] = 10000

    return answer

for i in range(len(fees)):
    solution(fees[i],records[i])