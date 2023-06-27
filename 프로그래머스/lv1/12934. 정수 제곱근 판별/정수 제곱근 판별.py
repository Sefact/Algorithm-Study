import math

def solution(n):
    square = math.sqrt(n)    
    return (int(square + 1)) ** 2 if square % 1 == 0 else -1