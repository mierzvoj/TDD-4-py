import unittest

from main import get_verse



class ChristmasCarol(unittest.TestCase):
    def test_single_ver_1(self):
        self.assertEqual(get_verse(0),
                         "On the first day of Christmas, my true love gave to me: a Partridge in a Pear Tree.")

    def test_single_ver_2(self):
        self.assertEqual(get_verse(1),
                         "On the second day of Christmas, my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_single_ver_3(self):
        self.assertEqual(get_verse(2),
                         "On the third day of Christmas, my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_single_ver_4(self):
        self.assertEqual(get_verse(3),
                         "On the fourth day of Christmas, my true love gave to me: "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")