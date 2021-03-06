import math

def is_composite_2_to_d(z, d):
    if d == 1:
        return False
    else:
        return ((z % d) == 0) or is_composite_2_to_d(z, d - 1)


def is_prime(y):
    '''
    Returns True if n is prime and false otherwise.

    is_prime: Nat -> Bool

    Examples:
       is_prime(0) => False
       is_prime(1) => False
       is_prime(2) => True
       is_prime(101) => True
    '''
    if y == 0 or y == 1:
        return False
    if y == 2:
        return True
    if is_composite_2_to_d(y, y - 1):
        return False
    else:
        return True

def is_prime_sq_divisor(b, c):
    if c >= math.sqrt(b) +1 :
        return False
    else:
        if is_prime(c):
            return ((b % c ** 2) == 0) or is_prime_sq_divisor(b, c + 1)
        else:
            return is_prime_sq_divisor(b, c + 1)

def is_squarefree(a, e):
    if (e >= math.sqrt (a) +1):
        return  False
    if is_prime_sq_divisor(a, e):
       answer1 = False
       return answer1
    else:
       answer1 = True
       return answer1 or is_squarefree(a, e + 1)

def number_of_prime_divisors(f,g,k):
    if f==1 or g >= (f//2 ) + 1 :
        return k
    else:
        if is_prime(g) and (f % g == 0):
            k = k + 1
        return number_of_prime_divisors(f, g+1, k)


def mobius(n):
    '''
        Returns xxxxx.

        Requires n > 0
    '''
    if not is_squarefree(n, 1):
        return 0
    else:
        l = number_of_prime_divisors(n, 1, 0)
        #print(number_of_prime_divisors (n, 1, 0))
        if (l != 0) and (l % 2 == 0):
            return 1
        else:
            return -1



print (is_squarefree(1, 1), mobius(1))
print (is_squarefree(12, 1), mobius(12))
print (is_squarefree(20349, 1), mobius(20349))
print (is_squarefree(6, 1), mobius(6))
print (is_squarefree(51, 1), mobius(51))
print (is_squarefree(74, 1), mobius(74))
print (is_squarefree(97, 1), mobius(97))
print (is_squarefree(811, 1), mobius(811))
