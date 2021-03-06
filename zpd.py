#!/usr/bin/python3
# Raspberry Pi - Zero Photography Device
# The **RPi-ZPD** is a very small device to make photos and 2K timelapse videos.
#
# (c)2017 P1X/kj

VERSION = '0.3'

from time import sleep
from dot import Dot  
from kbd import Kbd
from menu import Menu
from photo import Photo
from timelapse import Timelapse
from info import Info
from quitprogram import QuitProgram

if __name__ == '__main__':
    d = Dot()
    k = Kbd()
    m = Menu()
    p = Photo(d, k)
    i = Info(d, k)
    t = Timelapse(d, k, p)
    q = QuitProgram(d, k)

    # LOGO INTRO
    d.logo()
    sleep(1)

    # MAIN MENU
    while True:
        d.write(m.get_active_menu())

        k.read()
        if k.was('EXIT'):
            break
        elif k.was('UP'):
            m.set_menu_up()
        elif k.was('DOWN'):
            m.set_menu_down()
        elif k.was('ENTER'):
            if m.is_menu('PHOTO'):
                p.enter()
            elif m.is_menu('BATCH'):
                t.enter()
            elif m.is_menu('INFO'):
                i.enter()
            elif m.is_menu('QUIT'):
                q.enter()
            else:
                d.write('N/A')
                sleep(1)
