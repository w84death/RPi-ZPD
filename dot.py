import microdotphat as dot

class Dot:
    def __init__(self):
        dot.clear()
        dot.set_rotate180(True)
        dot.fill(1)
        dot.show()


    def write(self, msg):
        dot.clear()
        dot.write_string(msg, kerning=False)
        dot.show()

    def loop(self):
        dot.show()