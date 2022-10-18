import sys
sys.stdin = open('16506input.txt')

# opcodes.get(arr[0]) 이거를 써야 뒷값이 나옴

def thre(z):
    global a, b, c
    if z % 2 == 1:
        c = 1
        a = z // 2
    else:
        c = 0
        a = z // 2
    if a % 2 == 1:
        b = 1
        a = a // 2
    else :
        b = 0
        a = a // 2
    return a, b, c


N = int(input())
for tc in range(N):
    arr = list(map(str, input().split()))
    opcodes = {
        'ADD' : '0000',
        'SUB' : '0001',
        'MOV' : '0010',
        'AND' : '0011',
        'OR' : '0100',
        'NOT' : '0101',
        'MULT' : '0110',
        'LSFTL' : '0111',
        'LSFTR' : '1000',
        'ASFTR' : '1001',
        'RL' : '1010',
        'RR' : '1011',
    }
    # print(opcodes.get(arr[0]))
    # new_arr = arr[0]
    # if arr[0][len(arr[0])-1] == 'C':
    #     new_arr = (arr[0]+'C')
    # print(new_arr)
    # print (arr[0]+'C')
    # print (arr[0][len(arr[0])-1])
    # print (opcodes.get(new_arr))
    if arr[0][len(arr[0]) - 1] == 'C':
        new_arr = arr[0][0:len(arr[0])-1]
        print( opcodes.get(new_arr),sep='', end='')
    else:
        print(opcodes.get(arr[0]), sep='', end='')

    if arr[0][len(arr[0])-1] == 'C':
        print('1',sep='',end='')
    else:
        print('0',sep='',end='')
    print('0',sep='', end='')  # 5번자리
    # 0-7 이진수
    k = int(arr[1])
    thre(k)
    print(a,b,c,sep='',end='')
    # NOT랑 MOV 는 000 어차피 arr[2]가 0으로 나와서 따로 조건이 필요가없네
    # 원래 len(1) 이 O 라서 그거 가져오려함
    p = int(arr[2])
    if p == 0:
        print('000',sep='',end='')
    else:
        thre(p)
        print(a, b, c, sep='', end='')
    # 시작값이 C로 끝나는거면 rb 아니면 #C
    q = int(arr[3])
    if arr[0][len(arr[0])-1] == 'C':
        if q >=8:
            thre(q-8)
            print('1',a, b, c, sep='', end='')
        else:
            thre(q)
            print('0',a, b, c, sep='', end='')

    else:
        thre(q)
        print(a, b, c,'0', sep='', end='')

    print('')





