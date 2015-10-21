import pywinauto
import time

def init_wizard(): 
    try:
        pwa_app = pywinauto.application.Application()
        w_handle = pywinauto.findwindows.find_windows(title=u'stdin', class_name='MediaPlayerClassicW')[0]
        Wizard = pwa_app.window_(handle=w_handle)
        return Wizard
    except IndexError:
        raise 'App not find'


def get_position(app):
    pos = app.Rectangle()
    return pos.left, pos.top, pos.width(), pos.height()


def check_monitor(y_pos):
    '''Returns True if window is in the first (up) monitor'''
    return True if y_pos > 0 else False

def change_monitor():
    window = init_wizard()
    x_pos, y_pos, width, height = get_position(window)
    print(x_pos)
    if check_monitor(y_pos):
        window.MoveWindow(x=0, y=-1080, width=1920, height=1080)
    else:
        window.MoveWindow(x=0, y=0, width=1920, height=1080)

change_monitor()
