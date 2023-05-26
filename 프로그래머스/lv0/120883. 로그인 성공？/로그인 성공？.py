def solution(id_pw, db):
    answer = ""
    dicts = {i[0]: i[1] for i in db}
    
    if id_pw[0] in dicts:
        if id_pw[1] == dicts[id_pw[0]]:
            answer = "login"
        else:
            answer = "wrong pw"
    else:
        answer = "fail"
    
    return answer