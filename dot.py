import microdotphat as dot
from time import sleep

class Dot:
    def __init__(self):
        dot.clear()
        dot.set_rotate180(True)
        dot.fill(1)
        dot.show()
        

    def logo(self):
        dot.write_string('RPiZPD', kerning=False)
        dot.set_decimal(2, 1)
        sleep(1)

    def write(self, msg):
        dot.clear()
        dot.write_string(msg, kerning=False)
        dot.show()