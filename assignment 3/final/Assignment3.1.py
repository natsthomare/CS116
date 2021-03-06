import check

def unicode_encoding(s):
    '''
    Returns a valid unicode value in binary string format.

    unicode_encoding: Str -> Str
    Requires
     Length of s <=21

    Examples:
    unicode_encoding('101001') => '00101001'
    unicode_encoding('11101001') => '1100001110101001'
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

##Examples
check.expect("Example 1",unicode_encoding('101001'),'00101001')
check.expect("Example 2",unicode_encoding('11101001'),'1100001110101001')

##Tests
check.expect("t is 0",unicode_encoding('0'),'00000000')
check.expect("t = length is 1",unicode_encoding('1'),'00000001')
check.expect("t =  length is less than 7 digits",unicode_encoding('1234567'),'01234567')
check.expect("t =  length is 7 digits",unicode_encoding('1234567'),'01234567')
check.expect("t =   7 digits < length < 11 digits",unicode_encoding('00011111111'),'1100001110111111')
check.expect("t =  length is 11 digits",unicode_encoding('12345678910'),'1101234510678910')
check.expect("t =  11 digits < length < 16 digits",unicode_encoding('0001234567890123'),'111000011023456710890123')
check.expect("t =  length is 16 digits",unicode_encoding('1234567890123456'),'111012341056789010123456')
check.expect("t =  16 digits < length < 21 digits",unicode_encoding('000012345678901234567'),'11110000100123451067890110234567')
check.expect("t =  length is 21 digits",unicode_encoding('123456789012345678901'),'11110123104567891001234510678901')








