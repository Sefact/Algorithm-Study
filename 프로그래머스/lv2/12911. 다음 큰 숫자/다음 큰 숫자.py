def count_num(n):
    binary = bin(n)[2:]
    count = binary.count('1')
    return count

def solution(n):
    answer = count_num(n)

    while True:
        n += 1
        if count_num(n) == answer:
            return n