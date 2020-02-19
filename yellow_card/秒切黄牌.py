if(1):
    import tkinter as tk
    import os
    import subprocess


    window = tk.Tk()
    window.title('my window')
    window.geometry('200x300')

    #1
    var = tk.StringVar()
    #var.set('')
    var_1 = tk.StringVar()

    l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15,
                 height=2)
    # l = tk.Label(window, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)
    l.pack()

    def end_exe():
        #os.system("taskkill /F /IM yellow_card_test.exe")
        #os.system("taskkill /F /IM yellow_card.exe")

        cmd = "taskkill /F /IM yellow_card.exe"
        ret = subprocess.call(cmd, shell=True)
        var.set('')

        #from time import sleep
        #sleep(0.5)

        cmd = "taskkill /F /IM yellow_card_test.exe"
        ret = subprocess.call(cmd, shell=True)
        var_1.set('')

        print('end!')
        return 1


    on_hit = False
    def hit_me():
        global on_hit
        if on_hit == False:
            on_hit = True
            var.set('长按P键退出脚本！')
            subprocess.call('start yellow_card_test.exe', shell=True)

        else:
            on_hit = False
            end_exe()
            var.set('')

        #os.system('start yellow_card_test.exe')


    b = tk.Button(window, text='自动释放技能（测试用）', width=20,
                  height=2, command=hit_me)
    b.pack()


    #2

    l_1 = tk.Label(window, textvariable=var_1, bg='green', font=('Arial', 12), width=15,
                 height=2)
    # l_1 = tk.Label(window, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)
    l_1.pack()
    on_hit_1 = False
    def hit_me_1():
        global on_hit_1
        if on_hit_1 == False:
            on_hit_1 = True
            var_1.set('长按P键退出脚本！')
            subprocess.call('start yellow_card.exe', shell=True)
        else:
            on_hit_1 = False
            end_exe()
            var_1.set('')

        #os.system('start yellow_card.exe')


    b_1 = tk.Button(window, text='秒切黄牌', width=15,
                  height=2, command=hit_me_1)
    b_1.pack()





    b_2 = tk.Button(window, text='暂停程序', width=15,
                    height=2, command=end_exe)
    b_2.pack()


    window.mainloop()
    end_exe()



    # import subprocess
    # cmd = "taskkill /F /IM yellow_card.exe"
    # ret = subprocess.call(cmd, shell=True)
    #
    # cmd = "taskkill /F /IM yellow_card_test.exe"
    # ret = subprocess.call(cmd, shell=True)

    #CREATE_NO_WINDOW = 0x08000000
    #ret = subprocess.call(cmd, shell=True,creationflags=CREATE_NO_WINDOW)


    #