from ejercicio2 import evaluate_condition
import ejercicio2

def cgi_decoded_instrumented(s: str):
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
    hex_values = {ord(key): value for key, value in hex_values.items()}
    t=''
    i=0
    while evaluate_condition(1, "Lt", i, len(s)): #c1
        c=ord(s[i])
        if evaluate_condition(2, "Eq", c, ord('+')):#c2
            t += ' '
        elif evaluate_condition(3, "Eq", c, ord('%')):#c3
            digit_high, digit_low = ord(s[i+1]), ord(s[i+2])
            i += 2
            if evaluate_condition(4, "In", digit_high, hex_values) and evaluate_condition(5, "In", digit_low, hex_values):#c4
                v = hex_values[digit_high] * 16 + hex_values[digit_low]
                t += chr(v)
            else:
                raise ValueError('Invalid encoding')
        else:
            t+=chr(c)
        i+=1
    return t

import unittest

class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        ejercicio2.distances_true = {}
        ejercicio2.distances_false = {}
        return super().setUp()
    
    def test_1(self):
        self.assertEqual(cgi_decoded_instrumented("%00"), chr(0))
        self.assertDictEqual(ejercicio2.distances_true, {1: 0, 2: 6, 3: 0, 4: 0, 5: 0})
        
    
    def test_2(self):
        self.assertEqual(cgi_decoded_instrumented("%00+%00"), "\0 \0")
        self.assertDictEqual(ejercicio2.distances_true, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0})
        self.assertDictEqual(ejercicio2.distances_false, {1: 0, 2: 0, 3: 1, 4: 1, 5: 1})


    def test_3(self):
        with self.assertRaises(expected_exception=ValueError):
            cgi_decoded_instrumented("%invalid")
        self.assertDictEqual(ejercicio2.distances_true, {1: 0, 2: 6, 3: 0, 4: 3})
        self.assertDictEqual(ejercicio2.distances_false, {1: 8, 2: 0, 3: 1, 4: 0})


    def test_4(self):
        self.assertEqual(cgi_decoded_instrumented("This is %00"), "This is " + chr(0))
        self.assertDictEqual(ejercicio2.distances_true, {1: 0, 2: 6, 3: 0, 4: 0, 5: 0})
        self.assertDictEqual(ejercicio2.distances_false, {1: 0, 2: 0, 3: 0, 4: 1, 5: 1})


    def test_5(self):
        self.assertEqual(cgi_decoded_instrumented("Hello+Reader"), "Hello Reader")
        self.assertDictEqual(ejercicio2.distances_true, {1: 0, 2: 0 , 3: 35})
        self.assertDictEqual(ejercicio2.distances_false, {1: 0, 2: 0 , 3: 0})