def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.pop(arr.index(sorted(arr)[0]))
        return arr