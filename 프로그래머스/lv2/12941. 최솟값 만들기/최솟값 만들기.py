def solution(A,B):
    answer = [x * y for x, y in list(zip(sorted(A), sorted(B, reverse=True)))]

    return sum(answer)