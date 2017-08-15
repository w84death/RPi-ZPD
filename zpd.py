#!/usr/bin/python3
# Raspberry Pi - Zero Photography Device
# The **RPi-ZPD** is a very small device to make photos and 2K timelapse videos.
#
# (c)2017 P1X/kj

VERSION = '0.2'

from time import sleep
from dot import Dot  
from kbd import Kbd

if __name__ == '__main__':
    d = Dot()
    k = Kbd()

    d.logo()

    while True:
        k.read()
        if k.was('EXIT'):
            break
        elif k.was('UP'):
            d.write('UP')
        elif k.was('DOWN'):
            d.write('DOWN')
