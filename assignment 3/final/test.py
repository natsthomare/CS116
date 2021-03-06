def backwards(n):
    '''
    Returns the natural number n with the digits
    in the reversed order

    backwards: Nat -> Nat

    Examples:
       backwards(0) => 0
       backwards(10) => 1
       backwards(1234) => 4321
    '''
    return int(str(n)[::-1])
print(backwards(0))


