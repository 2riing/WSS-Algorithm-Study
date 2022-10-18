a, b = map(int, input().split())
c = int(input())

if b+c >= 60 :    # 분침이 60분을 넘을때
    a = a + ((b+c) // 60)  # 새로운 시침은 60을 넘어선 새로운 값을 a에 추가
    b = (b+c) % 60   # 새로운 분침은 60으로 나눈 나머짓값
    if a >= 24:   # a가 24시간이 넘으면 0시가 되야되므로  나머짓값
        a = a % 24
else:
    b = b+c
print(a,b)

print( 120 // 60)