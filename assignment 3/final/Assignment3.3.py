def parse_ip (ip, start):
        '''
        Returns the string ip from the start position until the first period.

        parse_ip: Str Int -> Str
        '''
        return ip[start:ip.find('.')]

def rev(x):
        '''
        Returns a 3 digit reverse string of x.

        rev: Str -> Str
        '''
        if len(x) == 3:
            y = x[2] + x [1] + x [0]
        elif len (x) == 2:
            y = x[1] + x [0] + '0'
        else:
            y = x[0] + '00'
        return y


def check_hacker (ip_value):
        '''
        Returns whether given ip value,in string format,is a hacker.

        check_hacker: Str -> Bool
        '''
        a = parse_ip(ip_value,0)
        dot_position = ip_value.find('.')
        if dot_position == -1:
            return False
        rest_ip = ip_value [dot_position+1:]
        b = parse_ip(rest_ip,0)
        dot_position = rest_ip.find('.')
        if dot_position == -1:
            return False
        rest_ip = rest_ip[dot_position + 1:]
        c = parse_ip(rest_ip,0)
        dot_position = rest_ip.find('.')
        if dot_position == -1:
            return False
        d = rest_ip[dot_position+1:]
        if a[0] == d[-1]:
            return True
        elif (rev(a) == b) or (rev (a) == c) or (rev (a) ==d):
            return True
        elif (rev(b) == a) or (rev (b) == c) or (rev (b) ==d):
            return True
        elif (rev(c) == a) or (rev (c) == b) or (rev (c) ==d):
            return True
        elif (rev(d) == a) or (rev (d) == b) or (rev (d) ==c):
            return True
        else:
            return False


def valid_ip (ip_value):
        '''
        Returns whether ip value is valid or not.

        valid_ip: Str -> Bool
        '''
        a = parse_ip(ip_value,0)
        dot_position = ip_value.find('.')
        if dot_position == -1:
            return False
        rest_ip = ip_value [dot_position+1:]
        b = parse_ip(rest_ip,0)
        dot_position = rest_ip.find('.')
        if dot_position == -1:
            return False
        rest_ip = rest_ip[dot_position + 1:]
        c = parse_ip(rest_ip,0)
        dot_position = rest_ip.find('.')
        if dot_position == -1:
            return False
        d = rest_ip[dot_position+1:]
        if (0 <= int(a) <= 255)  and (0 <= int(b) <= 255)  and \
                (0 <= int(c) <= 255)  and (0 <= int(d) <= 255):
            return True
        else:
            return False

def Enter_ip (i,t):
        '''
        Returns
        '''
        print("start",i)
        if i == t+1:
            print("print here",i)
            return
        else:
            n = False
            ip = input("Enter a valid IPv4 address:")
            if valid_ip (ip):
                print(ip,i,t)
                n=(check_hacker (ip))
                print(n)
                if n:
                   return n
                else:
                   return n
            else:
                print(ip,"Invalid IP address")
                Enter_ip(i+1, t)

def hacker():
        '''

        Requires

        '''
        x= Enter_ip (3,4)
        print(x)
        return x



print(hacker())





    #print(valid_ip ('0.0.0.0'))
    #print(valid_ip ('0.256.0.0'))
    #print(valid_ip ('0.0.256.0'))
    #print(valid_ip ('0.0.0.256'))
    #print(valid_ip ('0.256.256.0'))
    #print(valid_ip ('0.0.0'))
    #print(valid_ip ('0.0'))
    #print(valid_ip ('ww'))


    #print ('Valid IP but hacker as First digit same as last digit', check_hacker ('192.168.0.1'))
    #print ('Valid IP but hacker as rev number matches other number', check_hacker ('123.321.0.1'))
    #print ('Valid IP but hacker as rev number matches other number', check_hacker ('0.1.123.321'))
    #print ('Valid IP but hacker as rev number matches other number', check_hacker ('123.1.0.321'))
    #print ('Valid IP but hacker as rev number matches other number', check_hacker ('0.123.1.321'))
    #print ('Valid IP and no hacker ', check_hacker ('192.168.0.2'))




