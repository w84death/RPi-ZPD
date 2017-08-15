from time import sleep

class Info():
    def __init__(self, dot, kbd):
        self.d = dot
        self.k = kbd

    def enter(self):
        while True:
            self.d.write('P1X/kj')
            self.k.read()
            if self.k.was('BACK'):
                break
        return False