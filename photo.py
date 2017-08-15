from time import sleep

class Photo():
    def __init__(self, dot, kbd):
        self.d = dot
        self.k = kbd

    def enter(self):
        self.d.write('READY?')
        while True:
            self.k.read()
            if self.k.was('ENTER'):
                self.take()
            elif self.k.was('EXIT'):
                break
        return False

    def take(self):
        self.d.write('SNAP!')
        sleep(1)
        return True
