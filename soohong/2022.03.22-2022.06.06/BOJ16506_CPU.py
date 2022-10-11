import sys
sys.stdin = open('../0420/input.txt')

N = int(input())
words =[list(input().split()) for _ in range(N)]
# opcode / rD / rA / rB /

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


for word in words:
    rD, rA, C = word[1], word[2], word[3]

    result = ''
    flag = 0

    if word[0][-1] == 'C': # 마지막 글자가 C이면
        word[0] = word[0][:-1] # C를 잘라줌
        flag = 1
    if flag: # C가 있으면 다음글자 1임
        result += opcodes[word[0]]+'10' # opcode 값과 항상 0인 값 넣어줌
    else:
        result += opcodes[word[0]]+'00'

    # rD 이진수 변환
    rD =  str(bin(int(rD)))[2:]
    if len(rD) < 3:
        rD = '0'*(3-len(rD)) + rD
    result += rD

    # rA 이진수 변환 0일 때 처리
    if rA != '0':
        rA = str(bin(int(rA)))[2:]
        if len(rA) < 3:
            rA = '0' * (3 - len(rA)) + rA
        result += rA
    else:
        result += '000'
    # rA 글자수가 모자랄경우

    # rB or C 처리,
    if flag == 0: # rB사용
        C = str(bin(int(C)))[2:]
        if len(C) < 3:
            C= '0' * (3 - len(C)) + C
        result += C + '0'
    elif flag == 1: # C 사용
        C =  str(bin(int(C)))[2:]
        if len(C) < 4:
            C = '0' * (4 - len(C)) + C
        result += C



    print(result)