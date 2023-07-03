def solution(price, money, count):
    answer = [price * i for i in range(1, count + 1)]

    return 0 if money > sum(answer) else sum(answer) - money