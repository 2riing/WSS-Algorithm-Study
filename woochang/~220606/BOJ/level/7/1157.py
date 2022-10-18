S = input()
T = S.lower()

arr = [0]*26
print(ord('c'))

for i in range(len(T)):
    arr[ord(T[i])-96] += 1
max_a = 0
for j in range(arr):
    if max_a < arr[j]:
        max_a = arr[j]