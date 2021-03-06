import check
import math

def str_after_semicolon(n,iters,answer_string):
    if type (n) == int:
        answer_string = answer_string + "]"
        return answer_string
    if iters == 1:
        answer_string = answer_string + "...]"
        return answer_string
    else:
        m = n - (math.floor(n))
        reciprocal = 1 / m
        answer_string = answer_string  + str(math.floor(reciprocal)) + ","
        return str_after_semicolon(reciprocal, iters - 1, answer_string)

def continued_fraction(n,iters):
    answer_str = ""
    answer_str = "[" + (str(math.floor(n))) + ";" + str_after_semicolon(n,iters,answer_str)
    return answer_str

print(continued_fraction(math.e, 12))
print(continued_fraction(7, 12))
print (continued_fraction(math.pi + 2150, 1))
#print (continued_fraction(math.pi, 12))




