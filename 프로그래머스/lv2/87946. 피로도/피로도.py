from itertools import permutations

def solution(k, dungeons):
    answer = -1
    clears = []
    temp = list(permutations(dungeons, len(dungeons)))
    for i in temp:
        count = 0
        fatigue = k
        for j in i:
            if fatigue >= j[0]:
                fatigue -= j[1]
                count += 1
        clears.append(count)
    return (max(clears))