def solution(absolutes, signs):
    answer = [absolutes[i] if signs[i] else -absolutes[i] for i in range(0, len(absolutes))]
    
    return sum(answer)