word = input()

for i in range(len(word)):
    print(ord(word[i]) - 64, end=' ')
print()