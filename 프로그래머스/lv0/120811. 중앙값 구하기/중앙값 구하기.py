def solution(array):
    array = sorted(array) 
    idx = len(array)//2
    return (array[idx] + array[-idx - 1])/2