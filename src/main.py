import machine
import uasyncio
import urequests
import time
import ssd1306
import bitmaps

OLED_WIDTH = 128
OLED_HEIGHT = 64
SCROLL_PAUSE_TIME = 0
CHAR_WIDTH = 8
NUM_STOPS = 4  # number of stops to display on the screen


def setup_oled():
    i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))
    oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)
    return oled


oled = setup_oled()

username, password = open("creds", "r").read().split("\n")[:-1]


async def get_departures(stop_num="8011155", num_results=4):
    url = f"https://v6.db.transport.rest/stops/{stop_num}/departures?results={num_results}?remarks=false?nationalExpress=false?national=false?regionalExpress=false?regional=false?suburban=false?bus=false?ferry=false?subway=true?tram=false?taxi=false?pretty=false"

    while True:
        departures = urequests.request("GET", url, stream=True).json()["departures"]

        oled.fill(0)

        directions = [departure["direction"] for departure in departures]

        for _ in range(NUM_STOPS):
            scroll_pos = 0

            max_len_departure = max([len(direction) for direction in directions])

            max_scroll_pos = 0 - max_len_departure

            for i, scroll_pos in enumerate(reversed(range(max_scroll_pos, 1))):

                for row_num, direction in enumerate(directions):
                    if len(direction) * CHAR_WIDTH > OLED_WIDTH:
                        curr_x = scroll_pos
                    else:
                        curr_x = 0

                    for char in direction:
                        if char in bitmaps.de_bitmaps:
                            bitmaps.draw_de_char(
                                oled, char, curr_x, CHAR_WIDTH * row_num
                            )
                        else:
                            oled.text(char, curr_x, (CHAR_WIDTH * row_num) + 2, 1)
                        curr_x += 8

                oled.show()

                # if first pass, sleep for a bit so you can read the beginning of the text
                if i == 0:
                    time.sleep(1)
                oled.fill(0)
                time.sleep(SCROLL_PAUSE_TIME)
            time.sleep(2)


uasyncio.run(get_departures())
