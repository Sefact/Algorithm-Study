def ternary(n):
    res = ''
    while n > 0:
        remainder = n % 3
        res = str(remainder) + res
        n = n // 3
    return res

def decimal(n):
    decimal = 0
    count = 0

    for digit in reversed(n):
        decimal += int(digit) * (3 ** count)
        count += 1

    return decimal
    

def solution(n):
    answer = "".join(list(reversed(ternary(n))))
    return decimal(answer)