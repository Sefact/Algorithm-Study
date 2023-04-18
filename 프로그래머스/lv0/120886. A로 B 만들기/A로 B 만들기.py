def solution(before, after):
    answer = 0
    if ''.join(sorted(before)) == ''.join(sorted(after)):
        answer = 1
    else:
        answer = 0
    return answer