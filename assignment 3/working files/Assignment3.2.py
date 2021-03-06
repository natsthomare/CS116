def print_top_half(i,n):
    if i == n+1:
        return
    elif i < n:
        print(" " * i, "\\\\", " " * (n - i - 1), "|||||", " " * (n - i - 1), "//", " " * i)
        return print_top_half(i+1,n)
    else:
        print(" " * i, "\\\\", "|||||", "//", " " * i)
        return print_top_half(i + 1, n)

def print_bottom_half(i, n):
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

    Requires
        Lenght of input parameter s <=21
    '''
    print_top_half (0, n-1)
    print (" "*(n+3)+ "||o||")
    print_bottom_half(0, n-1)

x_wing(5)

x_wing(1)

x_wing(2)
