#Standard library
import sys
import os
import json
import random
import time
from glob import glob

#Third party Library
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import PyHook3

def onKeyboardEvent(event):
    # Monitor keyboard events
    # Forbidding all keyboard response by return False
    return False
    # print( "MessageName:", event.MessageName  )
    # print( "Message:", event.Message )
    # print( "Time:", event.Time  )
    # print( "Window:", event.Window  )
    # print( "WindowName:", event.WindowName    )
    # print( "Ascii:", event.Ascii, chr(event.Ascii)    )
    # print( "Key:", event.Key     )
    # print( "KeyID:", event.KeyID    )
    # print( "ScanCode:", event.ScanCode   )
    # print( "Extended:", event.Extended   )
    # print( "Injected:", event.Injected    )
    # print( "Alt", event.Alt     )
    # print( "Transition", event.Transition  )
    # print( "---"      )
    # return True


# Create a "hook" management object
hm = PyHook3.HookManager()
# Listen for all keyboard events
hm.KeyDown = onKeyboardEvent
# Set keyboard "hook"
hm.HookKeyboard()

root='C:\\Pycharmproject\\lock_screen\\'

class Lock_Widget(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        self.setWindowTitle("Lock_screen")
        self.setWindowFlags(
            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Dialog
        )  #FramelessWindowHint设置无边界框  WindowStaysOnTopHint窗口在最前面
        self.setWindowState(self.windowState() | Qt.WindowFullScreen)

        self.img_label = QtWidgets.QLabel(self)
        self.set_label_fillshow()
        self.img_label.setAlignment(Qt.AlignCenter)
        self.img_label.setFont(QtGui.QFont("Roman times",30,QtGui.QFont.Bold))
        self.First_load = True
        self.IF_close = False
        self.img_files = glob(root+'pictures\\*.jpg')
        self.startTimer(12000)

    def closeEvent(self, event):
        if self.IF_close:
            pass
        else:
            event.ignore()

    def timerEvent(self, event):
        if len(self.img_files) > 0:
            self.show_img(self.img_files[random.randint(0,len(self.img_files)-1)])

    def mousePressEvent(self, event):
        datafile = root+'Lock_screen_data.json'
        if self.First_load:
            if not os.path.exists(datafile):
                sys.exit(0)
            # compare set_time and now_time
            timenow = time.localtime(time.time())[:6]
            json_nownum = [int(i) for i in timenow]  # 获取当前时间，转化为时间列表 [2021, 7, 17, 21, 45, 35] 年月日时分秒
            with open(datafile) as json_file:
                self.json_setnum = json.load(json_file)  # 获取json时间，转化为时间列表

            time_reduce_list = [json_nownum[i] - self.json_setnum[i] for i in range(len(json_nownum))]
            for i in range(len(time_reduce_list)):
                if time_reduce_list[i] != 0:
                    if time_reduce_list[i] > 0:   # print(i, 'yes unlock')
                        self.IF_close = True
                        self.close()
                        break
                    if time_reduce_list[i] < 0: # print(i, 'time not reach')
                        self.First_load = False
                        self.img_label.setText('解锁时间为\n{}年{}月{}日 {}:{}'.format(self.json_setnum[0],
                                                                               self.json_setnum[1],
                                                                               self.json_setnum[2],
                                                                               self.json_setnum[3],
                                                                               self.json_setnum[4],
                                                                               self.json_setnum[5]))
                        break
        else:
            pass

    def show_img(self,img_path):
        pix = QtGui.QPixmap(img_path)
        self.img_label.setPixmap(pix)

    def show_text(self,str):
        self.img_label.setText(str)

    def set_label_fillshow(self):
        desktop = QtWidgets.QApplication.desktop()
        # 获取显示器分辨率大小
        screenRect = desktop.screenGeometry()
        height = screenRect.height()
        width = screenRect.width()
        self.img_label.setScaledContents(True)
        self.img_label.setGeometry(0,0,width,height)




if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(Qt.AA_DisableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    lock_widget = Lock_Widget(window)
    lock_widget.show()

    sys.exit(app.exec())