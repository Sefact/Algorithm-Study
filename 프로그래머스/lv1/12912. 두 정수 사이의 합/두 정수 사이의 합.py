def solution(a, b):
    a, b = sorted([a, b])
    answer = [i for i in range(a, b + 1)]
    return sum(answer)