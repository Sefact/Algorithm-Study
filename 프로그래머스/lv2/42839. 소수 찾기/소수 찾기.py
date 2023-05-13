from itertools import permutations

def decimal(n):
    if n < 2:
        return False
    
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    tmp = []
    res = []
    
    for i in range(1, len(numbers) + 1):
        tmp.extend(permutations(numbers, i))
        res = [int(''.join(i)) for i in tmp]
        
    for i in set(res):
        if decimal(int(i)):
            answer += 1
    
    return answer