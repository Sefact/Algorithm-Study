def solution(A, B):
    for count in range(len(A)):
        if A == B:
            return count
        A = A[-1] + A[:-1]

    return -1