import readchar


class Kbd():
    def __init__(self):
        self.keys = {
            'PAGE_UP': '\x1b\x5b\x35\x7e',
            'PAGE_DOWN': '\x1b\x5b\x36\x7e',
            'HOME': '\x1b\x5b\x48',
            'END': '\x1b\x5b\x46',
            'ENTER': '\x0d',
            'BACKSPACE': '\x7f',
            'EXIT': '*',

            'UP': '\x1b\x5b\x41',
            'DOWN': '\x1b\x5b\x42',
            'LEFT': '\x1b\x5b\x44',
            'RIGHT': '\x1b\x5b\x43'  
        }
        self.last_key = ''
        pass

    def read(self):
        self.last_key = readchar.readkey()

    def was(self, key):
        if self.last_key == self.keys[key]:
            return True
        else:
            return False