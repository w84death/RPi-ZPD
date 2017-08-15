from time import sleep, time
from picamera import PiCamera

class Photo():
    def __init__(self, dot, kbd):
        self.d = dot
        self.k = kbd
        self.c = PiCamera()
        
        self.c.resolution = (2592, 1944)
        self.c.rotation = 90
        self.c.hflip = True
        self.c.vflip = True

    def enter(self):
        while True:
            self.d.write('READY?')
            self.k.read()
            if self.k.was('ENTER'):
                self.take()
            elif self.k.was('BACK'):
                break
        return False

    def make_photo(self, path):
        self.c.capture(path)

    def take(self):
        self.d.write('...')
        image_id = int(time())
        self.make_photo('snaps/{id}.jpg'.format(id=str(image_id)))
        self.d.write('SNAP!')
        sleep(0.5)
        return True
