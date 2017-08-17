#!/usr/bin/python3

CMD_QUIT = 0
CMD_PHOTO = 1
CMD_BATCH = 2
CMD_SET_RATIO_4_3 = 3
CMD_SET_RATIO_16_9 = 4
CMD_SET_RATIO_1_1 = 5
CMD_SET_IDLE_3 = 6
CMD_SET_IDLE_5 = 7
CMD_SET_IDLE_10 = 8
CMD_INFO = 9

menu = {
    'RPiZPD': {
        'PHOTO': CMD_PHOTO,
        'BATCH': CMD_BATCH,
        'CONFIG': {
            'RATIO': {
                ' 4:3': CMD_SET_RATIO_4_3,
                '16:9': CMD_SET_RATIO_16_9,
                ' 1:1': CMD_SET_RATIO_1_1
            },
            'IDLE': {
                ' 3 SEC': CMD_SET_IDLE_3,
                ' 5 SEC': CMD_SET_IDLE_5,
                '10 SEC': CMD_SET_IDLE_10
            }
        },
        'INFO': CMD_INFO,
        'QUIT': CMD_QUIT
    }
}

def draw(tree):
    for title, lvl in tree.items():
        if not isinstance(lvl, dict):
            print('Execute {t}?'.format(t=title))
            cmd = input('[Y]es [N]o [B]ack> ')
            if cmd == 'y':
                print('EXECUTED')
            elif cmd == 'b':
                return
        else:
            print('Open {t}?'.format(t=title))
            cmd = input('[Y]es [N]o [B]ack> ')
            if cmd == 'y':
                draw(lvl)
            elif cmd == 'b':
                return
    draw(tree)

draw(menu)