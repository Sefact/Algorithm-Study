from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(list)
    
    for i in clothes:
        print(i)
        dic[i[1]].append(i[0])
    for j in dic:
        answer *= len(dic[j]) + 1
    
    return answer - 1