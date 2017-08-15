from time import sleep

class Photo():
    def __init__(self, dot, kbd):
        self.d = dot
        self.k = kbd

    def enter(self):
        while True:
            self.d.write('READY?')
            self.k.read()
            if self.k.was('ENTER'):
                self.take()
            elif self.k.was('BACK'):
                break
        return False

    def take(self):
        self.d.write('...')       
        sleep(1)
        self.d.write('SNAP!')
        sleep(1)
        return True
