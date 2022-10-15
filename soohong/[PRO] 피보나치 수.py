def solution(n):
    fib = [0 for _ in range(n + 1)]
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] % 1234567 + fib[i - 2] % 1234567

    return fib[n] % 1234567