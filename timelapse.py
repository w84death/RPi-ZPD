from time import sleep

class Timelapse():
    def __init__(self, dot, kbd):
        self.d = dot
        self.k = kbd
        self.photo_id = 0
        self.sleep_time = 3

    def enter(self):
        while True:
            self.d.write('READY?')
            self.k.read()
            if self.k.was('ENTER'):
                self.run()
            elif self.k.was('BACK'):
                break
        return False

    def take(self):
        self.d.write('...')
        sleep(1)
        self.photo_id += 1
        self.d.write('{id} OK'.format(id=self.photo_id))
        sleep(1)
        return True

    def run(self):
        while True:
            self.take()
            self.d.write('SLEEP')
            sleep(self.sleep_time)
