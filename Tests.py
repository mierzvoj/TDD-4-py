import unittest

from main import get_verse
from main import starts_ends


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

    def test_single_ver_9(self):
        self.assertEqual(get_verse(8),
                         "On the ninth day of Christmas, my true love gave to me: nine Ladies Dancing, "
                         "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_single_ver_10(self):
        self.assertEqual(get_verse(9),
                         "On the tenth day of Christmas, my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, "
                         "eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, "
                         "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_single_ver_11(self):
        self.assertEqual(get_verse(10),
                         "On the eleventh day of Christmas, my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, "
                         "nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_single_ver_12(self):
        self.assertEqual(get_verse(11),
                         "On the twelfth day of Christmas, my true love gave to me: twelve Drummers Drumming, "
                         "eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, "
                         "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, "
                         "two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_ver_range_1_to_2(self):
        self.assertEqual(starts_ends(0, 1),
                         "On the first day of Christmas, my true love gave to me: a Partridge in a Pear Tree.On the second day of Christmas, my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_ver_range_1_to_3(self):
        self.assertEqual(starts_ends(0, 2),
                         "On the first day of Christmas, my true love gave to me: a Partridge in a Pear Tree."
                         "On the second day of Christmas, my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.On the third day of Christmas, my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_ver_range_1_to_4(self):
        self.assertEqual(starts_ends(0, 3),
                         "On the first day of Christmas, my true love gave to me: a Partridge in a Pear Tree."
                         "On the second day of Christmas, my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the third day of Christmas, my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the fourth day of Christmas, my true love gave to me: "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_ver_range_1_to_5(self):
        self.assertEqual(starts_ends(0, 4),
                         "On the first day of Christmas, my true love gave to me: a Partridge in a Pear Tree."
                         "On the second day of Christmas, my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the third day of Christmas, my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the fourth day of Christmas, my true love gave to me: "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the fifth day of Christmas, my true love gave to me: five Gold Rings, four Calling Birds, "
                         "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         )

    def test_ver_range_1_to_6(self):
        self.assertEqual(starts_ends(0, 5),
                         "On the first day of Christmas, my true love gave to me: a Partridge in a Pear Tree."
                         "On the second day of Christmas, my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the third day of Christmas, my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the fourth day of Christmas, my true love gave to me: "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the fifth day of Christmas, my true love gave to me: five Gold Rings, four Calling Birds, "
                         "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the sixth day of Christmas, my true love gave to me: six Geese-a-Laying, five Gold Rings, "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         )

    def test_ver_range_1_to_7(self):
        self.assertEqual(starts_ends(0, 6),
                         "On the first day of Christmas, my true love gave to me: a Partridge in a Pear Tree."
                         "On the second day of Christmas, my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the third day of Christmas, my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the fourth day of Christmas, my true love gave to me: "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the fifth day of Christmas, my true love gave to me: five Gold Rings, four Calling Birds, "
                         "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the sixth day of Christmas, my true love gave to me: six Geese-a-Laying, five Gold Rings, "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the seventh day of Christmas, my true love gave to me: seven Swans-a-Swimming, "
                         "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                         "and a Partridge in a Pear Tree."
                         )

    def test_ver_range_1_to_8(self):
        self.assertEqual(starts_ends(0, 7),
                         "On the first day of Christmas, my true love gave to me: a Partridge in a Pear Tree."
                         "On the second day of Christmas, my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the third day of Christmas, my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the fourth day of Christmas, my true love gave to me: "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the fifth day of Christmas, my true love gave to me: five Gold Rings, four Calling Birds, "
                         "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the sixth day of Christmas, my true love gave to me: six Geese-a-Laying, five Gold Rings, "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the seventh day of Christmas, my true love gave to me: seven Swans-a-Swimming, "
                         "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                         "and a Partridge in a Pear Tree."
                         "On the eighth day of Christmas, my true love gave to me: eight Maids-a-Milking, "
                         "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, "
                         "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."

                         )

    def test_ver_range_1_to_9(self):
        self.assertEqual(starts_ends(0, 8),
                         "On the first day of Christmas, my true love gave to me: a Partridge in a Pear Tree."
                         "On the second day of Christmas, my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the third day of Christmas, my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the fourth day of Christmas, my true love gave to me: "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the fifth day of Christmas, my true love gave to me: five Gold Rings, four Calling Birds, "
                         "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the sixth day of Christmas, my true love gave to me: six Geese-a-Laying, five Gold Rings, "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the seventh day of Christmas, my true love gave to me: seven Swans-a-Swimming, "
                         "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                         "and a Partridge in a Pear Tree."
                         "On the eighth day of Christmas, my true love gave to me: eight Maids-a-Milking, "
                         "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, "
                         "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the ninth day of Christmas, my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, "
                         "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         )

    def test_ver_range_1_to_10(self):
        self.assertEqual(starts_ends(0, 9),
                         "On the first day of Christmas, my true love gave to me: a Partridge in a Pear Tree."
                         "On the second day of Christmas, my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the third day of Christmas, my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the fourth day of Christmas, my true love gave to me: "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the fifth day of Christmas, my true love gave to me: five Gold Rings, four Calling Birds, "
                         "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the sixth day of Christmas, my true love gave to me: six Geese-a-Laying, five Gold Rings, "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the seventh day of Christmas, my true love gave to me: seven Swans-a-Swimming, "
                         "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                         "and a Partridge in a Pear Tree."
                         "On the eighth day of Christmas, my true love gave to me: eight Maids-a-Milking, "
                         "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, "
                         "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the ninth day of Christmas, my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, "
                         "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the tenth day of Christmas, my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, "
                         "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."

                         )
    def test_ver_range_1_to_11(self):
        self.assertEqual(starts_ends(0, 10),
                         "On the first day of Christmas, my true love gave to me: a Partridge in a Pear Tree."
                         "On the second day of Christmas, my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the third day of Christmas, my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the fourth day of Christmas, my true love gave to me: "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the fifth day of Christmas, my true love gave to me: five Gold Rings, four Calling Birds, "
                         "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the sixth day of Christmas, my true love gave to me: six Geese-a-Laying, five Gold Rings, "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the seventh day of Christmas, my true love gave to me: seven Swans-a-Swimming, "
                         "six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, "
                         "and a Partridge in a Pear Tree."
                         "On the eighth day of Christmas, my true love gave to me: eight Maids-a-Milking, "
                         "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, "
                         "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the ninth day of Christmas, my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, "
                         "seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the tenth day of Christmas, my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, "
                         "three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                         "On the eleventh day of Christmas, my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, "
                         "nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, "
                         "four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."

                         )