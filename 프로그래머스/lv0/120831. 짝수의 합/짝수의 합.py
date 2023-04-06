def solution(n):
    answer = 0
    for i in range(n + 1):
        if (i + 1 != 1):
            print("i: ", i)
            if(i % 2 == 0):
                answer += i
    return answer