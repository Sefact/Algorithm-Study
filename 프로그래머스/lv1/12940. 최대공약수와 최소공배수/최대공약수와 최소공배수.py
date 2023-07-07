def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):
    return (x * y) // gcd(x, y)
    
def solution(n, m):
    return [gcd(n, m), lcm(n, m)]