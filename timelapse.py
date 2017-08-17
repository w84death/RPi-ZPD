from time import sleep, time

class Timelapse():
    def __init__(self, dot, kbd, cam):
        self.d = dot
        self.k = kbd
        self.c = cam
        self.photo_id = 0
        self.sleep_time = 10
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
        self.c.make_photo('timelapse/{batch}-{id}.jpg'.format(
            batch=self.batch_id,
            id=str(self.photo_id)))
        self.d.write('{} \o/'.format(self.photo_id))
        sleep(1)
        return True

    def run(self):
        while True:
            self.take()
            self.d.write('{} zzz'.format(self.photo_id))
            sleep(self.sleep_time/4)
            self.d.write('{} Zzz'.format(self.photo_id))
            sleep(self.sleep_time/4)
            self.d.write('{} ZZz'.format(self.photo_id))
            sleep(self.sleep_time/4)
            self.d.write('{} ZZZ'.format(self.photo_id))
            sleep(self.sleep_time/4)
            
