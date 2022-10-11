
n = 7
arr1 = [46, 33, 33 ,22, 31, 50, 12]
arr2 = [27 ,56, 19, 14, 14, 10, 1]

def solution(n, arr1, arr2):
    new_arr = [[] for _ in range(n)]
    arr = ''
    for i in range(n):
        temps = bin(arr1[i] | arr2[i])[2:]
        # 0b111 5
        if len(temps) < n:
            temps = '0'*(n-len(temps)) + temps
        for j in range(n):
            if temps[j] == '1':
                arr += '#'
            elif temps[j] == '0':
                arr += ' '
        new_arr[i] = arr
        arr = ''
    return new_arr

solution(n, arr1, arr2)