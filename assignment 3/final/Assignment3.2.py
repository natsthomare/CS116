import check

def print_top_half(i,n):
    '''
    Prints the top half of the X-wing formation\
    given n which is the number of lines in the top  half of the X-wing formation\
    and i which is the variable used as a line counter.

    print_top_half -> Int Int -> None
    Requires
        0 <= i < n
        n > 0
    '''
    if i == n+1:
        return
    elif i < n:
        print(" " * i, "\\\\", " " * (n - i - 1), "|||||", " " * (n - i - 1), "//", " " * i)
        return print_top_half(i+1,n)
    else:
        print(" " * i, "\\\\", "|||||", "//", " " * i)
        return print_top_half(i + 1, n)

def print_bottom_half(i, n):
    '''
    Prints the bottom half of the X-wing formation \
    given n which is the number of lines in the bottom  half of the X-wing formation\
    and i which is the variable used as a line counter.

    print_bottom_half -> Int Int -> None
    Requires
        0 <= i < n
        n > 0
    '''
    if i == n + 1:
        return
    elif i == 0:
        print(" " * (n-i), "//" , "|||||",  "\\\\", " " * (n-i))
        return print_bottom_half(i + 1, n)
    else:
        print(" " * (n - i), "//", " " * (i-1) , "|||||", " "  * (i-1), "\\\\", " " * (n - i))
        return print_bottom_half(i + 1, n)



def x_wing(n):
    '''
    Returns None and the X-wing formation given a positive integer n.

    x_wing: Int -> None
    Requires

    Examples:
    x_wing(1) -> None
    x_wing(5) -> None
    '''
    print_top_half (0, n-1)
    print (" "*(n+3)+ "||o||")
    print_bottom_half(0, n-1)

##Examples:
check.set_screen("X-wing with 3 rows with one top,bottom,and center row")
check.expect("Test 1", x_wing(1),None)

check.set_screen("X-wing with 11 rows with five top and bottom rows and one center row")
check.expect("Example 2", x_wing(5),None)

##Tests:
check.set_screen("X-wing with 3 rows with one top,bottom,and center row")
check.expect("Test 1", x_wing(1),None)

check.set_screen("X-wing with 5 rows with two top and bottom rows and one center row")
check.expect("Test 2", x_wing(2),None)

check.set_screen("X-wing with 11 rows with five top and bottom rows and one center row")
check.expect("Test 3", x_wing(5),None)

