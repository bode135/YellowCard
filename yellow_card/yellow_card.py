#import
if(1):
    #import time
    import numpy as np
    #from PIL import ImageGrab
    import win32api, win32gui, win32con
    from win32gui import MoveWindow
    #import pynput
    #from pynput.mouse import Button, Controller
    import time
    from scipy.stats import truncnorm
    def sleep(time):
        std = time/5
        err = truncnorm.rvs(time - 2*std, time + 2*std, size=1)
        time.sleep(time+err)

    from time import sleep

    def is_change(xy=(100, 374), original_color=(127, 127, 126)):
        now_color = get_color(xy[0], xy[1])
        # get_color(xy[0], xy[1])
        return not color_equal(now_color, original_color)


    def get_color(x, y,dc = win32gui.GetWindowDC(win32gui.GetDesktopWindow())):
        #img_11 = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))
        hdc_color = win32gui.GetPixel(dc, x, y)
        #return img_11.getpixel((0, 0))
        return hdc_color



    def color_equal(c1, c2):
        for i in range(3):
            if (c1[i] != c2[i]):
                return 0
        return 1



    #import os
    import win32com.client
    #os.system('regsvr32 djjj.dll /s')
    dm = win32com.client.Dispatch('dm.dmsoft')  # 调用大漠插件
    #print(dm.ver())  # 输出版本号
    def press_char(ch,t = 0.1):
        #dm.KeyDownChar(ch)
        # if(dm.GetKeyState(87)):
        #     dm.KeyUpChar(ch)
        #     sleep(0.05)
        #dm.KeyPressChar(ch)
        #sleep(0.02)
        #dm.KeyUpChar(ch)
        #sleep(0.02)
        #sleep(t)
        dm.KeyDownChar(ch)
        sleep(t)
        dm.KeyUpChar(ch)
    print('Ready!')


    class Ps:
        Time = 0.1

        Constant = 800
        ctrl = 17
        alt = 18
        shift = 16

        f1 = 112
        f2 = 113
        f3 = 114
        f4 = 116
        f5 = 117

        enter = 13
        space = 32


    ps = Ps()


    class Key:

        def __init__(self, key='k'):
            if (key.__class__.__name__ == 'str'):
                self.chr = key.upper()
            else:
                self.chr = 'None'
            self.ord = self.conv_ord(key)

        def __main__(self):
            return self.ord

        def conv_ord(self, key0):
            key = key0
            if (key.__class__.__name__ == 'str'):
                # key = key.upper()
                key = ord(key.upper())
            elif (key.__class__.__name__ == 'int'):
                if (key >= 0 and key <= 9):
                    key = str(key)
                    key = ord(key)
            return key

        def conv_chr(self, key):
            key = chr(key)
            return key

        def conv(self, key0):
            key = key0
            if (key == Ps.Constant):
                key = self.ord
            else:
                key = self.conv_ord(key)
            return key

        def state(self, key=Ps.Constant):
            key = self.conv(key)
            return dm.GetKeyState(key)

        def press(self, key0=Ps.Constant):
            key = self.conv_ord(key0)

            return dm.KeyPress(key)

        def down(self, key0=Ps.Constant):
            key = self.conv_ord(key0)

            return dm.KeyDown(key)

        def up(self, key0=Ps.Constant):
            key = self.conv_ord(key0)

            return dm.KeyUp(key)

        def down_up(self, key0=Ps.Constant, t=Ps.Time):
            key = self.conv_ord(key0)
            self.down(key)
            sleep(t)
            self.up(key)

        def dp(self, key=Ps.Constant, t=Ps.Time):
            self.down_up(key)

        def print_str(self, Str_0='0'):
            Str_s = ['ni hao ',
                     'wo bu tai hui wan a',
                     'wo zhi shi ge xiao xue sheng    ',
                     'dui bu qi    wo keng le ni men le  ',
                     'duibuqi  wo tai cai le   '
                     ] + list(Str_0)

            for j in Str_s:
                sleep(1)
                self.dp(ps.enter)
                for i in j:
                    sleep(0.3)
                    i = k.conv(i)
                    k.dp(i)
                # for i in str_tmp:
                #     sleep(0.3)
                #     i = k.conv(i)
                #     k.dp(i)
                self.dp(ps.enter)

        print(1)
    kk = Key()
#parament
if(1):

    # for i in range(3):orig_click(xy)
    xy = (825, 971)
    original_color = (197, 231, 0)

    #[3921380, ]
    yellow = [ 2023913, 1827305, 2023912, 2154985, 1172715, 910826, 58859]
    #yellow = [58859,59375,9375,910830, 1304045, 2089707 ,1893356 ,2089708 ,4117732 ,4444385 ,8709357]
    ##   59375  2105333  2765555  3029746  3623919    3492080   3491569  3623664  5076199  5340132  9348079  11252473 11881851
    hdc_yellow = 59375
    # if( (hdc_yellow  ) in yellow):
    #     print(1)
    # else:
    #     print(0)

    #hdc_yellow = 2105333
    hdc_blue = 14119544
    #Str = 'dm-python'
    Str = 'League of Legends (TM) Client'
    #Str = 'Chrome_RenderWidgetHostHWND'
    #class_name = 'RiotWindowClass'

    handle = win32gui.FindWindow(None, Str)
    while(1):
        try:
            handle = win32gui.FindWindow(None, Str)
            print('Find the Game!')
            break
        except:
            print('The program don''t found the Game!')
            sleep(1)


    # handle = win32gui.GetDesktopWindow()
    #handle = 2361912
    handle
    # win32gui.FindWindow(Str)
    # win32gui.FindWindow(None,530628)
    dc = win32gui.GetWindowDC(handle)

    # dc = 0
    dc
    # get_color(0,0)
    # win32gui.GetPixel(dc,xy[0],xy[1])

    from time import sleep

    #time.sleep(1)


    def stop_0(ch='g'):
        # ch = 'a'
        break0 = 0
        ch = ch.upper()
        if (dm.GetKeyState(ord(ch))):
            print('------- Stop! --------')
            break0 = (win32gui.MessageBox(0, 'Do you continue?', 'Stop!', 1) - 1)
            if (break0 == 1):
                print('------ Break!!! ---------')
            # return break0
        return break0


    def stop(ch='E'):
        # ch = 'a'
        break0 = False
        ch = ch.upper()
        if (dm.GetKeyState(ord(ch))):
            break0 = not break0
            sleep(0.1)
            # return break0
        return break0
    1

class t0_t1():
    def __init__(self):
        self.t0 = time.time()
        self.tmp = 0
        self.last_run = 0
    def already_run(self):
        self.last_run = time.time()
        return time.time() - self.t0
    def now(self):
        self.last_run = time.time()
        return time.time() - self.t0

    def now_last(self):
        return time.time() - self.last_run
#run

Char = ['Q','W','E','R','1']
break0 = break1 = True;i = 0
#tt0 = t0_t1();tt0.now()
while(1):
    t0 = time.time()

    # if(time.time() - tt0.last_run > 1):
    #     stop_0('n')ii
    #     tt0.now()

    sleep(0.01)
    i+=1
    if(i % 1000 == 0):
        print(i)
    # if(i%30 == 0 and dm.GetKeyState(87) == 0):
    #     if (stop('H')):
    #         break
    if(stop_0('p')):
        break
    if(i%30 == 0):
        try:
            h1 = win32gui.FindWindow(None, Str)
            if (h1 == 0):
                print('End !!!')
                break

            print('Continue')

        except:
            print('End !!!')

    # if(kk.state('0')and kk.state(18)):
    #     break1 = not break1
    #     if(break1):
    #         print('   Stop!')
    #     sleep(0.5)


    if(dm.GetKeyState(ord('W'))):
        break0 = True
    if (i%10 == 0 and stop('E') == True and dm.GetKeyState(18) == 0 and dm.GetKeyState(17) == 0):
        break0 = False
        #key = not key
        press_char('W',t = 0.01)
        sleep(0.01)

        hdc_color = win32gui.GetPixel(dc, xy[0], xy[1])
        if(hdc_color in yellow):
            press_char('W',t = 0.01)

        print(break0)
    if(break0 == True):
        continue

    # for i in range(50):
    #     sleep(0.1)
    #
    #     print(dm.GetKeyState(ord('E')))
    #break

    #cl.append(get_color(xy[0],xy[1]))
    #print(is_change(xy, original_color))
    #if(not is_change(xy, original_color)):

    hdc_color = win32gui.GetPixel(dc, xy[0], xy[1])

    print('-------', break0,'   ',hdc_color)
    # if (hdc_color == hdc_yellow):
    #     #print('     Yellow card!   ',hdc_color)
    #     press_char('W')
    #     t1 = time.time() - t0
    #     print('cost_time:  ',t1)
    #     break0 = not break0
    #     sleep(0.2)
    if( hdc_color in yellow):
        #print('     Yellow card!   ',hdc_color)
        press_char('W',t = 0.1)
        t1 = time.time() - t0
        print('cost_time:  ',t1)
        break0 = not break0
        sleep(0.2)
    else:
        #print('not Yellow')
        pass
    1


#if(0):
# import pandas as pd
#
# sleep(2)
# press_char('w',0.1)
# tt = t0_t1();ss = []
# while(tt.now()<5):
#     if(stop('p')):
#         break
#     sleep(0.02)
#     hdc_color = win32gui.GetPixel(dc, xy[0], xy[1])
#     ss.append(hdc_color)
#
#     print(hdc_color,int(tt.now()))
# print(pd.unique(ss).tolist())
# win32gui.GetPixel(dc, xy[0], xy[1])
#ss = [5,5,5,51,1,1,2,3,4,4]
#[4378847, 3921380, 2023913, 1827305, 2023912,
# 2154985, 1172715, 910826, 58859, 12802912, 2171127]

#[4378847, 3921380, 2023913, 1827305, 2023912,
# 2154985, 1172715, 910826, 58859, 12802912, 2171127]
