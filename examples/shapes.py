# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import time

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi hardware SPI config:

#DC = 23
#RST = 24
#SPI_PORT = 0
#SPI_DEVICE = 0

# Raspberry Pi software SPI config:
SCLK = 17
DIN = 18
DC = 27
RST = 23
CS = 22


# Beaglebone Black hardware SPI config:
# DC = 'P9_15'
# RST = 'P9_12'
# SPI_PORT = 1
# SPI_DEVICE = 0

# Hardware SPI usage:
# disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Software SPI usage (defaults to bit-bang SPI interface):
disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)


# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))

forever_pos = 30
love_pos = 15
is_up = 1
while True:

    forever_pos = forever_pos - 1
    if forever_pos < -30:
        forever_pos = 83

    love_pos = love_pos - is_up
    if love_pos < 12:
        is_up = -1
    if love_pos > 14:
        is_up = 1

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a white filled box to clear the image.
    draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)

    # Draw some shapes.
    font = ImageFont.truetype("PeanutMoney.ttf", 16)
    draw.text((5,15), 'Zhang', font=font)
    font2 = ImageFont.truetype('SPAIDERS.TTF', 20)
    draw.text((42,love_pos), 'z', font=font2)
    draw.text((60,15), 'Wu', font=font)

    draw.text((forever_pos,26), "forever", font=font)

    # Load default font.
    font = ImageFont.load_default()

    # Alternatively load a TTF font.
    # Some nice fonts to try: http://www.dafont.com/bitmap.php


    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(0.04)
