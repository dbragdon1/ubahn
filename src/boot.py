import socket

import machine
import network
import time

import esp
esp.osdebug(None)

import gc
gc.collect()

print('booting...')

def connect(username, password):
    board_led = machine.Pin(2, machine.Pin.OUT)
    board_led.value(0)
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)

    sta_if.connect(username, password)

    while not sta_if.isconnected():
        board_led.value(1)
        time.sleep(1)
        board_led.value(0)
        time.sleep(1)

    for _ in range(3):
        board_led.value(1)
        time.sleep(0.1)
        board_led.value(0)
        time.sleep(0.1)

    board_led.value(1)

    print(sta_if.ifconfig())

ssid, password = open("creds", "r").read().split("\n")[:-1]

connect(ssid, password)

print('Connection successful')

led = machine.Pin(2, machine.Pin.OUT)
