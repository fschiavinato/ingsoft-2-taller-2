def cgi_decode(s):
    '''DecodetheCGI−encodedstring‘s‘:
    ∗replace'+'by''
    ∗replace'%xx'bythecharacterwithhexnumberxx.
    Returnthedecodedstring.Raise‘ValueError‘forinvalidinputs.
    '''
    #Mapping of hex digits to their integer values
    hex_values={
        '0':0,'1':1,'2':2,'3':3,'4':4,
        '5':5,'6':6,'7':7,'8':8,'9':9,
        'a':10,'b':11,'c':12,'d':13,'e':14,'f':15,
        'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,
    }
    t=''
    i=0
    while i < len(s):#c1
        c=s[i]
        if c=='+':#c2
            t+=' '
        elif c=='%':#c3
            digit_high, digit_low= s[i+1], s[i+2]
            i += 2
            if digit_high in hex_values and digit_low in hex_values:#c4
                v= hex_values[digit_high] * 16 + hex_values[digit_low]
                t+=chr(v)
            else:
                raise ValueError('Invalid encoding')
        else:
            t+=c
        i+=1
    return t


import unittest

class TestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(cgi_decode("%00"), chr(0))

    def test_2(self):
        self.assertEqual(cgi_decode("%00+%00"), "\0 \0")

    def test_3(self):
        with self.assertRaises(expected_exception=ValueError):
            cgi_decode("%invalid")

    def test_4(self):
        self.assertEqual(cgi_decode("This is %00"), "This is " + chr(0))

