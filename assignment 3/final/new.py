import check


def countup(n):
    '''
    Returns a list of the first n+1 natural numbers

    countup: Nat -> (listof Nat)

    Examples:
       countup(0) => [0]
       countup(5) => [0, 1, 2, 3, 4, 5]
    '''
    L = []
    if n == 0:
        L = [0]
        return L
    elif n == 1:
        L = [0, 1]
        return L
    else:
        L.extend(countup(n - 1))
        return L.append(n)


check.expect("Test", countup(5), [0, 1, 2, 3, 4, 5])