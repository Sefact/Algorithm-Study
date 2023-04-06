def solution(slice, n):
    count = 1
    while (slice * count // n) < 1:
        count += 1
    
    return count