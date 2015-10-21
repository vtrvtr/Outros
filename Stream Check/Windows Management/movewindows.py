import pywinauto
import time

def init_wizard(): 
    pwa_app = pywinauto.application.Application()
    w_handle = pywinauto.findwindows.find_windows(title=u'stdin', class_name='MediaPlayerClassicW')[0]
    Wizard = pwa_app.window_(handle=w_handle)
    return Wizard


def get_position(app):
    pos = app.Rectangle()
    return pos.left, pos.top, pos.width(), pos.height()


def check_monitor(y_pos):
    '''Returns True if window is in the first (up) monitor'''
    return True if y_pos < 0 else False


try:
    window = init_wizard()
    x_pos, y_pos, width, height = get_position(window)
    print(check_monitor(y_pos))

    # window.MoveWindow(x=0, y=-1080, width=1920, height=1080)
except Exception as e:
    print(e)