from collections import deque

def solution(prices):
    answer = []
    dq = deque(prices)
    
    while dq:
        price = dq.popleft()
        sec = 0
        for q in dq:
            sec += 1
            if price > q:
                break 
        answer.append(sec)
    
    return answer