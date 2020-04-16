'''
当时基于这份源代码开发其它功能,
所以有很多冗余没有去除,
秒切黄牌在最后实现.
建议从后往前看

                        by bode
'''
if(1):
    from time import time
    from time import sleep
    from random import randint
    from random import random

    if (1):
        import win32api, win32gui, win32con
        from win32gui import MoveWindow
        import win32com.client

        dm = win32com.client.Dispatch('dm.dmsoft')  # 调用大漠插件
        dm.ver()

    # Class
    if (1):
        class Mouse():
            def LeftClick(self):
                dm.LeftClick()

            def LeftDoubleClick(self):
                dm.LeftDoubleClick()

            def LeftDown(self):
                dm.LeftDown()

            def LeftUp(self):
                dm.LeftUp()

            def RightDown(self):
                dm.RightDown()

            def RightUp(self):
                dm.RightUp()

            def RightClick(self):
                dm.RightClick()

            def click_l(self, delay=0.1):
                self.LeftDown()
                sleep(delay)
                self.LeftUp()

            def click_r(self, delay=0.1):
                self.RightDown()
                sleep(delay)
                self.RightUp()

            def move_ab(a, b, t=1, tmp=0.01):
                times = int(t / tmp)
                times
                t0 = time.time()
                a, b
                for i in range(times):
                    x = a[0] + int((b[0] - a[0]) / times * (i + 1))
                    y = a[1] + int((b[1] - a[1]) / times * (i + 1))
                    # print(x,y)
                    mouse.position = (x, y)
                    sleep(tmp)
                return time.time() - t0

            def move_to(self, x, y=-1):
                print(x, y)
                if (y == -1):
                    dm.MoveTo(x[0], x[1])
                else:
                    dm.MoveTo(x, y)

                return 1

            1


        ms = Mouse()


        def stop(ch='E'):
            # ch = 'a'
            break0 = False
            ch = ch.upper()
            if (dm.GetKeyState(ord(ch))):
                break0 = not break0
                sleep(0.1)
                # return break0
            return break0


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
        1
    delay = 0.1;
    stop_ch = 'p';
    ch = 'g'
    while (0):
        sleep(delay)
        if (stop(stop_ch)):
            break

        if (kk.state(ch)):
            # print('press!')
            ms.click_r()
        else:
            print(0)


    if (1):
        def stop_0(ch='1'):
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


        def click(x=0):
            # move_mouse
            # click
            dm.LeftDown()
            rd = random()
            sleep(x + rd)
            dm.LeftUp()
            pass


        def click_r(x=0):
            # move_mouse
            # click
            dm.RightDown()
            rd = random()
            sleep(x + rd)
            dm.RightUp()
            pass


        def left_click(x, y):
            move_mouse(x, y)
            sleep(random() / 2)
            click()
            sleep(random() / 2)


        def right_click(x, y):
            move_mouse(x, y)
            sleep(random() / 2)
            click_r()
            sleep(random() / 2)


        def move_mouse(x, y):
            # move_aside_mouse
            rd_x = randint(5, 15)
            rd_y = randint(1, 10)
            # dm.MoveTo(x , y)
            xx, yy = (x + rd_x, y + rd_y)
            dm.MoveTo(xx, yy)
            return (xx, yy)


        def reset_mouse(t=0, x=2000, y=2000):
            move_mouse(x, y)
            sleep(t + random() / 2)


        def findpic(pic_name, re_mouse=1, t=0.5):
            global run_ed
            path = 'picture\\pic_renwu\\'
            if (stop_0('0')):
                print('stop!', run_ed)
                return 0

            if (re_mouse):
                reset_mouse(t)

            pic_end = '.bmp'
            name = path + pic_name + pic_end
            return dm.FindPic(0, 0, 2000, 2000, name, '101010', 0.9, 0)


        def have_pic(pic_name, re_mouse=1, t=0.5):
            i, x, y = findpic(pic_name, re_mouse, t)
            # findpic('buy_0')
            if (i == -1):
                # print(pic_name,0)
                return 0
            else:
                # print(pic_name,1)
                return 1


        def click_pic(pic_name, re_mouse=1, t=0.5):

            i, x, y = findpic(pic_name, re_mouse, t)

            if (i == -1):
                print('Click ', pic_name, ' Error!')
                return 0  # 点击图片失败
            if (i == 0):
                left_click(x, y)
                sleep(random() / 2)
                return 1  # 点击图片成功
            else:
                print('Click ', pic_name, ' Error!')
                return 0


        def right_click_pic(pic_name, re_mouse=1, t=0.5):
            i, x, y = findpic(pic_name, re_mouse, t)

            if (i == -1):
                print('R-Click ', pic_name, ' Error!')
                return 0  # 点击图片失败
            if (i == 0):
                right_click(x, y)
                sleep(random() / 2)
                return 1  # 点击图片成功
            else:
                print('Click ', pic_name, ' Error!')
                return 0


        1


    class Time():
        def __init__(self):
            self.t0 = time()
            self.t1 = time()
            self.now()

        def now(self):
            self.t1 = time()
            return self.t1 - self.t0

        def exceed(self, T):
            if (self.now() >= T):
                return 1
            else:
                return 0

        1


    delay = 0.01;
    stop_ch = 'p';
    ch = 'r';
    T = 1111

    tt = Time()
    while (0):

        if (tt.exceed(T)):
            break
        if (stop_0(stop_ch)):
            break

        if (kk.state(ch)):
            # print('press!')
            pic_name = 'weizhi_diren_1'
            i, x, y = findpic(pic_name, re_mouse=0)
            # ms.move_to(x, y)
            if (i == -1):
                continue
            ms.move_to(x + 40, y + 100)
            ms.click_r(0.01)
            print('---')

        else:
            print('已运行时间：', tt.now())

        sleep(delay)
        pass
    # gp
    if (0):
        right_click_pic('weizhi_wo')
        right_click_pic('weizhi_diren')
        pic_name = 'weizhi_wo'
        # pic_name = 'weizhi_diren'
        pic_name = 'weizhi_diren_0'
        pic_name = 'weizhi_diren_1'
        findpic(pic_name, re_mouse=0)
        i, x, y = findpic(pic_name, re_mouse=0)
        # ms.move_to(x, y)

        ms.move_to(x + 40, y + 100)

    ###

    #
    # address_s  = ['2a9ec0','320','8','0','8','5560']
    # #int('5560',16)
    # def sum_add(address_s):
    #     s = 0
    #     for add in address_s:
    #         hex_add = int(add,16)
    #         #print(hex_add)
    #         s += hex_add
    #     return s
    # s = sum_add(address_s)
    # hex(s)
    # s

    from time import time
    from time import sleep
    from random import randint
    from random import random

    # 导入大漠
    if (1):
        import win32api, win32gui, win32con
        from win32gui import MoveWindow
        import win32com.client

        dm = win32com.client.Dispatch('dm.dmsoft')  # 调用大漠插件
        dm.ver()



    1
#

########################## 核心 ######################################

if(1):
    #findpic('a_0',re_mouse=0)

    def findpic(pic_name, re_mouse=1, t=0.5):
        global run_ed
        path = 'picture\\pic_renwu\\'
        if (stop_0('0')):
            print('stop!', run_ed)
            return 0

        if (re_mouse):
            reset_mouse(t)

        pic_end = '.bmp'
        name = path + pic_name + pic_end

        x1,y1 = (1820,0)
        x2,y2 = (1920,50)
        return dm.FindPic(x1,y1,x2,y2, name, '101010', 0.9, 0)
    def have_pic(pic_name, re_mouse=1, t=0.5):
        i, x, y = findpic(pic_name, re_mouse, t)
        # findpic('buy_0')
        if (i == -1):
            # print(pic_name,0)
            return 0
        else:
            # print(pic_name,1)
            return 1

    delay = 0.01;
    delay_click = 0.01;
    stop_ch = 'p';
    ch = 'e';
    T = 600

    tt = Time();sleep(1)
    while (1):

        if (tt.exceed(T)):
            break
        if (stop_0(stop_ch)):
            break

        # if (kk.state(ch)):
        #     # print('press!')
        #     pic_name = 'weizhi_diren_1'
        #     i, x, y = findpic(pic_name, re_mouse=0)
        #     # ms.move_to(x, y)
        #     if (i == -1):
        #         continue
        #     ms.move_to(x + 40, y + 100)
        #     ms.click_r(0.01)
        #     print('---')

        # 代码核心: 如果有pic,就按一下
        if(have_pic('a_0',re_mouse=0) or have_pic('a_4',re_mouse=0) or have_pic('a_7',re_mouse=0)):

            #sleep(delay_click)
            kk.dp(ch,0.01)
            sleep(delay_click)
            kk.dp(ch, 0.01)

            print('--click--')
            sleep(1)

        else:
            print('已运行时间：', tt.now())

        sleep(delay)
        pass

#pp
