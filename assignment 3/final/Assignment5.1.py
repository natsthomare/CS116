def replace(n,a,b,exp, ans):
  if n < 10:
    if n == a:
        n = b
    ans = ans + n * (10**exp)
    return ans
  else:
    rem = n % 10
    quot = n // 10
    if rem == a:
        rem = b
    ans = ans + rem * (10**exp)
    exp = exp +1
    return replace(quot, a, b, exp, ans)



def replace_digits(n, a, b):
  '''
  Returns the number of zeros at the end of a number

  replace_digits: Nat Nat Nat -> Nat

  Examples:
    count_zeros(0) => 1
    count_zeros(1234) => 0
  '''
  exp = 0
  ans = 0
  return replace(n,a,b,exp,ans)

print(replace_digits(511, 1, 3))