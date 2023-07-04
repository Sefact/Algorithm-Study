def solution(a, b):
    answer = [a[i] * b[i] for i in range(0, len(a))]
    
    return sum(answer)