def solution(s):
    if len(s) == 4 or len(s) == 6:
        return False if sorted(s, reverse=True)[0].isalpha() else True
    else:
        return False