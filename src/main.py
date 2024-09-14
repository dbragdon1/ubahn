import machine
import uasyncio
import urequests
import gc
import network
import time
import ssd1306

username, password = open("creds", "r").read().split("\n")[:-1]


OLED_WIDTH = 128
OLED_HEIGHT = 64
SCROLL_PAUSE_TIME = 0
CHAR_SIZE = 8


def setup_oled():
    i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))
    oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)
    return oled


def connect(username, password):
    board_led = machine.Pin(2, machine.Pin.OUT)
    board_led.value(0)
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)

    sta_if.connect(username, password)

    oled.text("Connecting...", 0, 0)
    oled.show()

    while not sta_if.isconnected():
        board_led.value(1)
        time.sleep(1)
        board_led.value(0)
        time.sleep(1)

    oled.fill(0)

    for _ in range(3):
        board_led.value(1)
        time.sleep(0.1)
        board_led.value(0)
        time.sleep(0.1)

    board_led.value(1)


oled = setup_oled()

connect(username, password)


async def get_departures(stop_num="8011155", num_results=4):
    url = f"https://v6.db.transport.rest/stops/{stop_num}/departures?results={num_results}?remarks=false?nationalExpress=false?national=false?regionalExpress=false?regional=false?suburban=false?bus=false?ferry=false?subway=true?tram=false?taxi=false?pretty=false"

    while True:
        departures = urequests.request("GET", url, stream=True).json()["departures"]

        oled.fill(0)

        directions = [departure["direction"] for departure in departures]

        for _ in range(4):
            scroll_pos = 0

            max_len_departure = max([len(direction) for direction in directions])

            for i, scroll_pos in enumerate(reversed(range(0 - max_len_departure, 1))):
                for j, direction in enumerate(directions):
                    if len(direction) * CHAR_SIZE > OLED_WIDTH:
                        oled.text(direction, scroll_pos, CHAR_SIZE * j)
                    else:
                        oled.text(direction, 0, CHAR_SIZE * j)
                oled.show()
                # if first pass, sleep for a bit so you can read the beginning of the text
                if i == 0:
                    time.sleep(1)
                oled.fill(0)
                time.sleep(SCROLL_PAUSE_TIME)
            time.sleep(2)


uasyncio.run(get_departures())
