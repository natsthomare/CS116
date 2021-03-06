def unicode_encoding(s):
    '''

    Requires
        Length of input parameter s <=21
    '''
    length = len(s)
    if length <= 7:
        st = str(0)*(7-len(s)) + s
        st1 = '0' + st
        print (st, st1)
        return st1
    elif length <= 11:
        st = str(0)*(11-len(s)) + s
        print (st, st[:5])
        st1 = '110' + st[0:5]
        st2 = '10' + st[5:]
        st_final = st1 + st2
        print(st, st1, st2, st_final)
        return st_final
    elif length <= 16:
        st = str(0)*(16-len(s)) + s
        print(st)
        st1 = '1110' + st[:4]
        st2 = '10' + st[4:10]
        st3 = "10" + st[10:]
        st_final = st1 + st2 + st3
        print(st, st1, st2, st3, st_final)
        return st_final
    elif length <= 21:
        st = str(0) * (21 - len(s)) + s
        print(st)
        st1 = '11110' + st[:3]
        st2 = '10' + st[3:9]
        st3 = "10" + st[9:15]
        st4 = "10"+ st[15:]
        st_final = st1 + st2 + st3 + st4
        print(st, st1, st2, st3, st4, st_final)
        return st_final

print('t  is 0')
t = '0'
print(t, unicode_encoding(t))


print ('t = length is 1')
t = '1'
print(t, unicode_encoding(t))

t = '123456789012345678901'
print('t =  length is less than 7 digits')
t = '111111'
t = '123456'
print(t, unicode_encoding(t))


t = '123456789012345678901'
print('#t =  length is 7 digits')
t = '1111111'
t = '1234567'
print (t, unicode_encoding(t))

t = '123456789012345678901'
print('#t =   7 digits < length < 11 digits')
t = '11111111'
print(t, unicode_encoding(t))

t = '123456789012345678901'
print('#t =  length is 11 digits')
t = '11111111111'
t = '12345678910'
print(t, unicode_encoding(t))

t = '123456789012345678901'
print('#t =   11 digits < length < 16 digits')
t = '1111111111111'
t = '1234567890123'
print(t, unicode_encoding(t))

t = '123456789012345678901'
print('#t =  length is 16 digits')
t = '1111111111111111'
t = '1234567890123456'
print(t, unicode_encoding(t))

t = '123456789012345678901'
print('#t =   16 digits < length < 21 digits')
t = '11111111111111111'
t = '12345678901234567'
print(t, unicode_encoding(t))

t = '123456789012345678901'
print('#t =   length is 21 digits')
t = '111111111111111111111'
t = '123456789012345678901'
print(t, unicode_encoding(t))
