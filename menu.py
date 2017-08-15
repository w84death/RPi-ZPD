class Menu():
    def __init__(self):
        self.items = [
            'PHOTO',
            'BATCH',
            'CONFIG',
            'INFO',
            'QUIT'
        ]
        self.active_item = 0

    def get_active_menu(self):
        return self.items[self.active_item]

    def set_menu_up(self):
        self.active_item -= 1
        if self.active_item < 0:
            self.active_item = len(self.items) - 1

    def set_menu_down(self):
        self.active_item += 1
        if self.active_item >= len(self.items):
            self.active_item = 0

    def is_menu(self, item):
        return self.get_active_menu() == item
