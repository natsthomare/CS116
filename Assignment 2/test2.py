s = 'abcde 1 2   3 ab    '
t = s.find('a')
print(t)

s = 'abcde 1 2   3 ab    '
t = s.find('a', 1)
print(t)

s = 'xyz'
t = s.find('w' or 'x')
print(t)

s = 'abcde 1 2   3 ab    '
t = s.startswith('abc')
print(t)

s = 'abcde 1 2   3 ab    '
t = s.count('a')
print(t)

s = 'abcde 1 2   3 ab    '
t = s.replace(' ', '')
print(t)

s = 'abcde 1 2   3 ab    '
t = s.strip()
print(t)

s = 'abcde 1 2   3 ab    '
t = s.count('B')
print(t)

s = 'abc3e 1 2   3 ab    '
t = s.rfind('3')
print(t)

s = 'abcde 1'
t = s.capitalize()
print(t)

s = 'ABC'
t = s.isupper()
print(t)

s = 'ABC123@'
t = s.isupper()
print(t)

s = '2342936498610b7a'
t = s.strip('0123456789')
print(t)

s = 'aBcD'
t = s.lower()
print(t)

s = 'aaaaa'
t = s[1:-1].count('a')
print(t)

s = 'aA2@@'
t = s[:-2].isalnum()
print(t)

s = 'aA2@@'
t = s.index('@')
print(t)

s = 'a' * 3 +  'b' * 2
t = s[2:4]
s = s[1:] + t.upper()
s = s + t
print(s)

def greeting(name, activity, hr):
  t = 'Dear {1},\nWhat are you {0} at {2}:00?'
  s = t.format(activity, name, hr)
  print(s)

greeting('Student', 'eating', 5)