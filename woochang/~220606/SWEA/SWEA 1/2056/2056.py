import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    year = str(input())
    month = 10*int(year[4]) + int(year[5])
    date = 10*int(year[6]) + int(year[7])
    yyyy = 1000*int(year[0]) + 100*int(year[1]) + 10*int(year[2]) + int(year[3])
    ans = 0
    if month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        if date > 31:
            ans = -1
        elif date == 0:
            ans = -1
        else: pass
    elif month == (4 or 6 or 9 or 11):
        if date > 30:
            ans = -1
        elif date == 0:
            ans = -1
        else: pass
    elif month == 2:
        if date > 28:
            ans = -1
        elif date == 0:
            ans = -1
    elif month == 0:
        ans = -1
    elif month > 12:
        ans = -1
    else: pass
    if ans != -1:
        ans = f'{yyyy}/{month}/{date}'
    print(f'#{tc} {ans}')
