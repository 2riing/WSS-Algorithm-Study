N = input()

def dial(N):
    cnt = 0
    if N == 'A' or N == 'B' or N == 'C':
        cnt +=3
    elif N == 'D' or N == 'E' or N == 'F':
        cnt +=4
    elif N == 'G' or N == 'H' or N =='I':
        cnt +=5
    elif N == 'J' or N == 'K' or N == 'L':
        cnt +=6
    elif N == 'M' or N == 'N' or N == 'O':
        cnt +=7
    elif N =='P' or N == 'Q' or N== 'R' or N=='S':
        cnt +=8
    elif N=='T' or N=='U' or N=='V':
        cnt +=9
    elif N == 'W' or N=='X' or N=='Y' or N=='Z':
        cnt +=10
    return cnt

ccnt = 0
for i in range(len(N)):
    ccnt += dial(N[i])
print(ccnt)