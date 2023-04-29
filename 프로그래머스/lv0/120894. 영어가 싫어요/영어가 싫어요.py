def solution(numbers):
    array = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for idx, number in enumerate(array):
        numbers = numbers.replace(number, str(idx))
    return int(numbers)