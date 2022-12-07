verses = [["first", "and a Partridge in a Pear Tree."],
          ["second", "two Turtle Doves, "],
          ["third", "three French Hens, "],
          ["fourth", "four Calling Birds, "],
          ["fifth", "five Gold Rings, "],
          ["sixth", "six Geese-a-Laying, "],
          ["seventh", "seven Swans-a-Swimming, "],
          ["eighth", "eight Maids-a-Milking, "],
          ["ninth", "nine Ladies Dancing, "],
          ["tenth", "ten Lords-a-Leaping, "],
          ["eleventh", "eleven Pipers Piping, "],
          ["twelfth", "twelve Drummers Drumming, "]
          ]


def get_verse(line):
    opener = f"On the {verses[line][0]} day of Christmas, my true love gave to me: "
    verse = "".join(str(verses[i][1]) for i in range(line, -1, -1))
    return opener + (verse.replace("and ", "") if line == 0 else verse)


def starts_ends(start_verse, end_verse):
    if isinstance(start_verse, int) or isinstance(end_verse, int):

        return "".join(get_verse(line_n)
                   for line_n in range(start_verse, end_verse + 1))
    else:
        raise ValueError("input integer")


if __name__ == "__main__":
    print(starts_ends("a", "b"))
