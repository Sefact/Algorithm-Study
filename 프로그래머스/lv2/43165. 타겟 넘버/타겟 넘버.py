from collections import deque
def solution(numbers, target):
    answer = 0
    dq = deque()
    n = len(numbers)
    dq.append([numbers[0],0])
    dq.append([-1*numbers[0],0])
    while dq:
        temp, idx = dq.popleft()
        idx += 1
        if idx < n:
            dq.append([temp+numbers[idx], idx])
            dq.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer