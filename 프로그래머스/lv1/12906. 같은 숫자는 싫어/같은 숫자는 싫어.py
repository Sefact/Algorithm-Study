def solution(arr):
    answer = []
    for item in arr:
        if answer[-1:] == [item]: continue
        answer.append(item)
    return answer