import unittest

from main import get_verse



class ChristmasCarol(unittest.TestCase):
    def test_single_ver_1(self):
        self.assertEqual(get_verse(0),
                         "On the first day of Christmas, my true love gave to me: a Partridge in a Pear Tree.")
