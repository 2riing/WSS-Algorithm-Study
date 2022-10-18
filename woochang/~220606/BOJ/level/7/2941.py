N = input()

new_N = 'a' + N + 'aa'
cnt = len(new_N)
for i in range(1,len(new_N)-1):
    if new_N[i] == 'c':
        if new_N[i+1] == '=':
            cnt -=1
        if new_N[i+1] == '-':
            cnt -=1
    if new_N[i] == 'd':
        if new_N[i+1] == '-':
            cnt -=1
        if new_N[i+1] == 'z' and new_N[i+2] == '=':
            cnt -=2
    if new_N[i] == 'l':
        if new_N[i+1] == 'j':
            cnt -=1
    if new_N[i] == 'n':
        if new_N[i+1] == 'j':
            cnt -=1
    if new_N[i] == 's':
        if new_N[i+1] == '=':
            cnt -=1
    if new_N[i] == 'z':
        if new_N[i-1] == 'd':
            pass
        elif new_N[i+1] == '=':
            cnt -=1
print(cnt)