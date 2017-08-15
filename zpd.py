#!/usr/bin/python3
# Raspberry Pi - Zero Photography Device
# The **RPi-ZPD** is a very small device to make photos and 2K timelapse videos.
#
# (c)2017 P1X/kj

VERSION = 'pre-alpha 0.1'

import time 
import readchar

from dot import Dot  

if __name__ == '__main__':
    d = Dot()

    d.write('RPi-ZPD')

    while True:
        key = readchar.readkey()
        #d.loop()
