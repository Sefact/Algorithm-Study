def calc_bin(n):
    bin = ''
    while n > 0:
        bin = str(n % 2) + bin
        n = n // 2
    return bin

def solution(s):
    x, y = 0, 0
    
    while s != '1':
        x += 1
        y += s.count('0')
        s = s.replace('0', '')
        s = calc_bin(len(s))
    
    return [x, y]