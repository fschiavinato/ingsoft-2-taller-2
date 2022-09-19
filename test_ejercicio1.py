import unittest

from ejercicio1 import cgi_decode


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
