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
    a = len(s)
    b = s.count(" ")
    if s == "":
        t = "contains {0} characters, {1} spaces, and ends with '{2}'"
        u = t.format(0, 0, "")
        print(u)
    else:
        t = "contains {0} characters, {1} spaces, and ends with '{2}'"
        u = t.format(a, b, s[len(s) - 1])
        print(u)
    return None

a = analyze_string("Bananas are ripe!")
b = analyze_string("")
c=analyze_string(" ")