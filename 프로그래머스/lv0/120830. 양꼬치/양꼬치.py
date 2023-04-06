def solution(n, k):
    juice = 0
    if (n >= 10):
        juice = n // 10
    return ((n * 12000) + (k * 2000) - (juice * 2000))