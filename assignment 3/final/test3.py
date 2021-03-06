def dec_to_bin_calc(n,s):

    if n == 0:
        return s
    if n % 2 == 1:
        s =  "1" + s
        n = (n-1) // 2
        print(n, s)
        return dec_to_bin_calc(n,s)
    else:
        s =  "0" +s
        n = n // 2
        print(n, s)
        return dec_to_bin_calc(n,s)


def dec_to_bin(n):
    '''
    Returns the binary string equivalent of the decimal number n.

    dec_to_bin: Nat -> Str

    Examples:
       dec_to_bin(0) => "0"
       dec_to_bin(1) => "1"
       dec_to_bin(5) => "101"
       dec_to_bin(37) => "100101"
    '''
    if n <= 1:
        return str(n)
    return dec_to_bin_calc(n,"")

print(dec_to_bin(37))