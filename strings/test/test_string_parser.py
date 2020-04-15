import unittest
from string_parser import left_justify, justify_line

class LeftJustifyTestCase(unittest.TestCase):

    def test_left_justify_one_word(self):
        result = left_justify("testing", 10)
        self.assertTrue(len(result) == 10)
        self.assertEqual(result, "testing   ")

    def test_left_justify_line(self):
        result = left_justify("the text line to be left-justified", 40)
        self.assertTrue(len(result) == 40)
        self.assertEqual(result, "the text line to be left-justified      ")

    def test_left_justify_wrong_line(self):
        with self.assertRaises(ValueError) as context:
            left_justify(40, 40)
        self.assertEqual("Wrong line value was passed to be left-justified", str(context.exception))

    def test_left_justify_no_width(self):
        with self.assertRaises(ValueError) as context:
            left_justify("the text line to be left-justified", None)
        self.assertEqual("No line width was passed to lef-justify", str(context.exception))


class JustifyLineTestCase(unittest.TestCase):

    def test_justify_small_line_even_spaces(self):
        result = justify_line("the light was very good", 40)
        self.assertTrue(len(result) == 40)

    def test_justify_small_line_odd_spaces(self):
        result = justify_line("the light was good", 40)
        self.assertTrue(len(result) == 40)

    def test_justify_big_line_even_spaces(self):
        result = justify_line("Morbi massa leo, consequat euismod", 40)
        self.assertTrue(len(result) == 40)

    def test_justify_big_line_odd_spaces(self):
        result = justify_line("Morbi massa leo, consequat nec euismod", 40)
        self.assertTrue(len(result) == 40)