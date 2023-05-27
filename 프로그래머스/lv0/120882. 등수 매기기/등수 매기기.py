def solution(score):
    scores = [i[0] + i[1] for i in score]
    tmp = sorted(scores, reverse=True)
    score_dict = {}
    
    for idx, val in enumerate(tmp):
        if val not in score_dict:
            score_dict[val] = idx + 1
            
    answer = [score_dict[i] for i in scores]
    
    return answer