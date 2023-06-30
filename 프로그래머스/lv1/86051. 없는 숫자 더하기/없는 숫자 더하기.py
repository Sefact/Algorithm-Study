def solution(numbers):
    numsArr = [i for i in range(0, 10)]
    answer = [i for i in numsArr if i not in numbers]
    return sum(answer)