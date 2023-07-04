def solution(left, right):
    arr = [i for i in range(left, right + 1)]
    temp = 0
    answer = 0
    
    for idx in arr:
        temp = [i for i in range(1, idx + 1) if idx % i == 0 ]
        if len(temp) % 2 == 0:
            answer += idx
        else:
            answer -= idx
    
    return answer