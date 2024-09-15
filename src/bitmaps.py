de_bitmaps = {
    "ä": [
        "        ",
        "        ",
        "  1  1  ",
        "        ",
        "  1111  ",
        "     11 ",
        "  11111 ",
        " 11  11 ",
        "  11111 ",
    ],
    "Ö": [
        "  1  1  ",
        "        ",
        "  1111  ",
        " 11  11 ",
        " 11  11 ",
        " 11  11 ",
        " 11  11 ",
        " 11  11 ",
        "  1111  ",
    ],
    "Ä": [
        "  1  1  ",
        "        ",
        "   11   ",
        "  1111  ",
        " 11  11 ",
        " 111111 ",
        " 11  11 ",
        " 11  11 ",
        " 11  11 ",
    ],
    "ö": [
        "        ",
        "        ",
        "  1  1  ",
        "        ",
        "  1111  ",
        " 11  11 ",
        " 11  11 ",
        " 11  11 ",
        "  1111  ",
    ],
    "ü": [
        "        ",
        "        ",
        "  1  1  ",
        "        ",
        " 11  11 ",
        " 11  11 ",
        " 11  11 ",
        " 11  11 ",
        "  1111  ",
    ],
    "Ü": [
        "  1  1  ",
        "        ",
        " 11  11 ",
        " 11  11 ",
        " 11  11 ",
        " 11  11 ",
        " 11  11 ",
        " 11  11 ",
        "  1111  ",
    ],
    "ß": [
        "        ",
        "        ",
        " 11111  ",
        " 11  11 ",
        " 11111  ",
        " 11  11 ",
        " 11  11 ",
        " 11 11  ",
        " 11     ",
    ],
}


def draw_de_char(oled, char, x, y):
    for row, line in enumerate(de_bitmaps[char]):
        for col, pixel in enumerate(line):
            if pixel == "1":
                oled.pixel(x + col, y + row, 1)


# oled.text("Gr", 0, 2)
# draw_umlaut(CHAR_SIZE * 2, 0, "ü")
# draw_umlaut(CHAR_SIZE * 3, 0, "Ü")
# oled.text("Uu", CHAR_SIZE * 4, 2)
# draw_umlaut(CHAR_SIZE * 6, 0, "Ö")
# oled.text("O", CHAR_SIZE * 7, 2)
# draw_umlaut(CHAR_SIZE * 8, 0, "ö")
# oled.text("o", CHAR_SIZE * 9, 2)
# oled.text("a", CHAR_SIZE * 10, 2)
# oled.text("A", CHAR_SIZE * 11, 2)
# draw_umlaut(CHAR_SIZE * 12, 0, "ä")
# draw_umlaut(CHAR_SIZE * 13, 0, "Ä")
# oled.text("Hei ", CHAR_SIZE * 4, 12)
# draw_umlaut(CHAR_SIZE * 7, 10, "ß")
# oled.text("B", CHAR_SIZE * 8, 12)
# oled.show()
