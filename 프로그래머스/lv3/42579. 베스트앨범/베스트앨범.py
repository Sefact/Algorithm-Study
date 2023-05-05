def solution(genres, plays):
    answer = []
    
    temp1 = {}
    temp2 = {}
    
    for index, (genres, plays) in enumerate(zip(genres, plays)):
        # type dictionary
        if genres not in temp1:
            temp1[genres] = [(index, plays)]
        else:
            temp1[genres].append((index, plays))
        # plays total
        if genres not in temp2:
            temp2[genres] = plays
        else:
            temp2[genres] += plays
        
    for key, value in sorted(temp2.items(), key=lambda x : x[1], reverse=True):
        for (index, plays) in sorted(temp1[key], key=lambda x : x[1], reverse=True)[:2]:
            answer.append(index)
    
    return answer