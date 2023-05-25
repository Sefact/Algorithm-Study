def solution(spell, dic):
    answer = 2
    
    for i in dic:
        if not set(spell) - set(i):
            answer = 1
    
    return answer