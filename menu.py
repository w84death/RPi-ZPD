class Menu():
    def __init__(self):
        self.items = [
            'PHOTO ',
            'TIME L',
            'CONFIG',
            'INFO'
        ]
        self.active_item = 0

    def get_active_menu(self):
        return self.items[self.active_item]

    def set_menu_up(self):
        self.self.active_item -= 1
        if self.active_item < 0:
            self.active_item = len(self.items) - 1

    def set_menu_down(self):
        self.self.active_item += 1
        if self.active_item > len(self.items):
            self.active_item = 0