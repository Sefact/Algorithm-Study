def solution(my_string, num1, num2):
    storeA = my_string[num1]
    storeB = my_string[num2]
    arr = list(my_string)
    arr[num1] = storeB
    arr[num2] = storeA
    arr = "".join(arr)
    return arr