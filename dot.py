import microdotphat as dot

class Dot:
    def __init__(self):
        pass

    def write(self, msg):
        dot.clear()
        dot.write_string(msg)
        dot.show()
