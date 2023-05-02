def solution(balls, share):
    return int(factorial_func(balls) / int(factorial_func((balls - share)) * factorial_func(share)))

def factorial_func(n):
    return n * factorial_func(n - 1) if n > 1 else 1