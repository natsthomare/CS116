def backwards_step(processing, acc):
    '''
    Appends the last digit of processing to the end of acc.

    backwards_step: Nat Nat -> Nat

    Examples:
       backwards_step(567, 8) => 87
       backwards_step(56, 87) => 876
       backwards_step(5, 876) => 8765
    '''
    return (acc * 10) + (processing % 10)