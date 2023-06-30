def solution(s):    
    sLen = len(s)
    return s[sLen // 2] if sLen % 2 == 1 else s[(sLen // 2)-1:(sLen // 2)+1]