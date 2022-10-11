import sys
sys.stdin = open('../0504/input.txt')


mo_list = ['a', 'e', 'o', 'u', 'i']

def IsMo(password):
    for aeiou in mo_list:
        if aeiou in password:
            return 1

def Double(password):
    for i in range(len(password) - 1):
        if password[i] == password[i+1]:
            if password[i] == 'o' or password[i] == 'e':
                pass
            else:
                return 1

def Triple(password):
    mo = 0
    ja = 0
    for word in password:
        if mo == 3 or ja == 3:
            return 1
        if word in mo_list:
            mo += 1
            ja = 0
        else:
            ja += 1
            mo = 0
    if mo == 3 or ja == 3:
        return 1


while True:
    pw = input()
    password = list(pw)
    is_mo_exist = 0
    is_double = 0
    is_triple = 0

    bad = 'is not acceptable.'
    good = 'is acceptable.'

    if pw == 'end':
        break
    else:
        is_double = Double(password)
        if is_double:
            print(f'<{pw}> '+bad)
        else:
            is_triple = Triple(password)
            if is_triple:
                print(f'<{pw}> '+bad)
            else:
                is_mo_exist = IsMo(password)  # 모음이 있으면 1
                if is_mo_exist:
                    print(f'<{pw}> '+ good)
                else:
                    print(f'<{pw}> ' + bad)



