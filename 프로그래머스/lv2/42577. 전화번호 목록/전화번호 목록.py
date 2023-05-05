def solution(phone_book):
    answer = True
    obj = {}
    for i in phone_book:
        obj[i] = i
    for j in phone_book:
        temp = ""
        for number in j:
            temp += number
            if temp in obj and temp != j:
                answer = False
    return answer