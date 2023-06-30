def solution(x):
    harshad = [int(i) for i in str(x)]    
    return True if x % sum(harshad) == 0 else False