import microdotphat as dot

class Dot:
    def __init__(self):
        dot.clear()
        dot.set_rotate180(True)

    def write(self, msg):
        dot.clear()
        dot.write_string(msg)
        dot.show()

    def loop(self):
        dot.show()