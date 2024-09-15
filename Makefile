run:
	ampy --port /dev/ttyUSB0 run src/main.py
load:
	ampy --port /dev/ttyUSB0 put src/main.py
	ampy --port /dev/ttyUSB0 put src/boot.py
	ampy --port /dev/ttyUSB0 put src/bitmaps.py
	ampy --port /dev/ttyUSB0 put deps/ssd1306.py
load_credentials:
	ampy --port /dev/ttyUSB0 put creds
flash:
	esptool.py --port /dev/ttyUSB0 erase_flash
	esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 115200 write_flash -z 0x1000 ./ESP32_GENERIC-20240222-v1.22.2.bin
