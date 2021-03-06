def analyze_string(s):
    '''
    Prints to the screen:
    contains C characters, P spaces, and ends with E.
    where:
    C is the length of s,
    P is the number of spaces (' ') in s
    E is the last character in s.

    Effects:
       Prints to screen

    analyze_string: Str -> None

    Examples:
       analyze_string("") => None
       and prints
       contains 0 characters, 0 spaces, and ends with ''.

       analyze_string("Bananas are ripe!") => None
       and prints
       contains 17 characters, 2 spaces, and ends with '!'.
    '''
    t="contains {0} characters, {1} spaces, and ends with '{2}'."
    u=t.format(len(s), s.count(" "), s[-1])
    print (u)

analyze_string("Bananas are ripe!")