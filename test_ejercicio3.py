import unittest

from ejercicio3 import cgi_decoded_instrumented
import ejercicio2


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
        self.assertDictEqual(ejercicio2.distances_true, {1: 0, 2: 0, 3: 35})
        self.assertDictEqual(ejercicio2.distances_false, {1: 0, 2: 0, 3: 0})
