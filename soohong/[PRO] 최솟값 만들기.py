from itertools import permutations

def solution(A, B):
    answer = 1000 * 1000
    N = len(A)
    permusA = list(permutations(A, N))
    permusB = list(permutations(B, N))
    print(permusA)
    print(permusB)
    for i in range(len(permusA)):
        for j in range(len(permusA)):# permutaions 길이
            temp = 0
            for k1 in range(N):
                temp += (permusA[i][k1] * permusB[j][k1])
        if answer > temp:
            answer = temp
    return answer

solution([1, 2], [3, 4])