import sys
sys.stdin = open('input.txt')

#A-Z 65-90 / a-z 97-122

def ROTA(word): #대문자
    if ord(word)+13 > 90:
        return chr(ord(word) + 13 - 26)
    else:
        return chr(ord(word) + 13)
def ROTa(word):# 소문자
    if ord(word)+13 > 122:
        return chr(ord(word) + 13 - 26)
    else:
        return chr(ord(word) + 13)

words = input()

for word in words: # 알파벳 범위에 속한다면
    if (ord(word)>=65 and ord(word)<=90): # 대문자일 때
        print(ROTA(word),end='')
    elif(ord(word)>=97 and ord(word)<=122): # 소문자일 때
        print(ROTa(word),end='')
    else:
        print(word, end='')
