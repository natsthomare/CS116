def gcd_countdown(m,n,x):
    if x == 1:
        return 1
    else:
        if ((n % x) == 0) and ((m % x) == 0):
            return x
        else:
            return  gcd_countdown(m,n, x- 1)

def gcd(m, n):
    '''
    Returns the greatest common divisor of m and n

    gcd: Int Int -> Nat

    Examples:
       gcd(0, 0) => 0
       gcd(3, 6) => 3
       gcd(-2, -10) => 2
    '''
    if m == 0 or n == 0:
        return 0
    return gcd_countdown(m,n,min(abs(m),abs(n)))
print(gcd(7777,9999))

