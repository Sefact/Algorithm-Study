def solution(emergency):
    answer = []
    count = 1
    for i in emergency:
        for j in emergency:
            if (i != j and i < j):
                count += 1
        answer.append(count)
        count = 1
    return answer