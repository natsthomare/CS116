def check_duplicates(L,i):
    if i == L[0]:
        return False
    else:
        return True



def filter_duplicates_of_first(L):
    '''
    Returns a list like L except any duplicates of the
    first element are removed.

    filter_duplicates_of_first: (listof Any) -> (listof Any)
    Requires: L is non-empty

    Examples:
       filter_duplicates_of_first([10]) => [10]
       filter_duplicates_of_first([1, 11, 2, 1, 1, 5, 4, 1])
          => [1, 11, 2, 5, 4]
       filter_duplicates_of_first([0, 11, 2, 1 ,1, 5, 4, 1])
          => [0, 11, 2, 1, 1, 5, 4, 1]
    '''
    return [L[0]] + list(filter(lambda i: check_duplicates(L,i),L[1:]))
print(filter_duplicates_of_first([0, 11, 2, 1 ,1, 5, 4, 1]))