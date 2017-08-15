import microdotphat as dot

class Dot:
    def __init__(self):
        dot.clear()
        dot.set_rotate180(True)
        dot.fill(1)
        dot.show()        

    def logo(self):
        dot.write_string('RPiZPD', kerning=False)
        dot.set_decimal(2, 1)
        return True

    def write(self, msg):
        dot.clear()
        dot.write_string(msg, kerning=False)
        dot.show()
        return True