def solution(my_string, queries):
    arr = list(my_string)
    
    for i in queries:
        tmp = arr[i[0]:i[1]+1]
        arr[i[0]:i[1]+1] = tmp[::-1]
    
    return "".join(arr)