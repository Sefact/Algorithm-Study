def solution(phone_number):
    answer = ''
    
    if len(phone_number) == 4:
        answer = phone_number[-4:]
    else:
        answer = '*' * (len(phone_number) - 4) + phone_number[-4:]
    
    return answer