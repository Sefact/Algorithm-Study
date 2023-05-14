def solution(quiz):
    answer = []
    
    for q in quiz:
        l, r = q.split('=')
        l = l.split()
        if l[1] == '+':
            if (int(l[0]) + int(l[2])) == int(r):
                answer.append("O")
            else:
                answer.append("X")
        elif l[1] == '-':
            if (int(l[0]) - int(l[2])) == int(r):
                answer.append("O")
            else:
                answer.append("X")
    return answer