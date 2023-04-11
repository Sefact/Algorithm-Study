def solution(array):
    answer = []
    stack = 0
    index = 0
    for i in range(0, len(array)):
        if array[i] > stack:
            stack = array[i];
            index = i;
    answer.append(stack)
    answer.append(index)
    return answer