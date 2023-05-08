def solution(sizes):
    w, h = 0, 0
    for i in sizes:
        i.sort()
        w = max(w, i[0])
        h = max(h, i[1])
    
    return w * h