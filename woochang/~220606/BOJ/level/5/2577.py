A = int(input())
B = int(input())
C = int(input())
ar = A* B * C
arr = str(A * B * C)
bucket = [0] * 10
for i in range(len(bucket)):
    for j in range(len(arr)):
        if i == int(arr[j]):
            bucket[i] += 1
    print(bucket[i])