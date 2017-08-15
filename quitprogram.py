import os
from time import sleep

class QuitProgram():
    def __init__(self, dot, kbd):
        self.d = dot
        self.k = kbd

    def enter(self):
        while True:
            self.d.write('SHURE?')
            self.k.read()
            if self.k.was('ENTER'):
                self.d.write('BYE :)')
                sleep(1)
                os.system("shutdown now -h")
            elif self.k.was('BACK'):
                break
        return False
