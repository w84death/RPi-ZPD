from time import sleep, time
from picamera import PiCamera

class Timelapse():
    def __init__(self, dot, kbd):
        self.d = dot
        self.k = kbd
        self.c = PiCamera()
        self.c.resolution = (2592, 1944)
        self.c.rotation = 90
        self.c.hflip = True
        self.c.vflip = True
        self.photo_id = 0
        self.sleep_time = 3
        self.batch_id = int(time())

    def enter(self):
        while True:
            self.d.write('READY?')
            self.k.read()
            if self.k.was('ENTER'):
                self.batch_id = int(time())
                self.run()
            elif self.k.was('BACK'):
                break
        return False

    def take(self):
        self.d.write('...')
        sleep(1)
        self.photo_id += 1
        self.c.capture('timelapse/{batch}{id}.jpg'.format(
            batch=self.batch_id,
            id=str(self.photo_id)))

        self.d.write('{id} OK'.format(id=self.photo_id))
        sleep(1)
        return True

    def run(self):
        while True:
            self.take()
            self.d.write('SLEEP')
            sleep(self.sleep_time)
            