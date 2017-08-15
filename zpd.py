#!/usr/bin/python3
# Raspberry Pi - Zero Photography Device
# The **RPi-ZPD** is a very small device to make photos and 2K timelapse videos.
#
# (c)2017 P1X/kj

VERSION = '0.2'

from time import sleep
from dot import Dot  
from kbd import Kbd
from menu import Menu

if __name__ == '__main__':
    d = Dot()
    k = Kbd()
    m = Menu()

    d.logo()

    while True:
        k.read()
        d.write(m.get_active_menu())
        if k.was('EXIT'):
            d.write('BYE :)')
            sleep(1)
            break
        elif k.was('UP'):
            m.set_menu_up()
        elif k.was('DOWN'):
            m.set_menu_down()
        
