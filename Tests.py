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

    def test_single_ver_5(self):
        self.assertEqual(get_verse(4),
                         "On the fifth day of Christmas, my true love gave to me: five Gold Rings, four Calling Birds, "
                         "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_single_ver_6(self):
        self.assertEqual(get_verse(5),
                         "On the sixth day of Christmas, my true love gave to me: six Geese-a-Laying, five Gold Rings, "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_single_ver_7(self):
        self.assertEqual(get_verse(6),
                            "On the seventh day of Christmas, my true love gave to me: seven Swans-a-Swimming, "
                            "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                            "and a Partridge in a Pear Tree.")

    def test_single_ver_8(self):
        self.assertEqual(get_verse(7),
                         "On the eighth day of Christmas, my true love gave to me: eight Maids-a-Milking, "
                         "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, "
                         "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")