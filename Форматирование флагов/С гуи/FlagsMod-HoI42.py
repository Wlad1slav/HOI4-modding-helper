# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PIL import Image
import os, sys, time
from colorama import init, Fore


class Formater(QThread):
    def __init__(self, Form, parent=None):
        super().__init__()
        self.ui = Form

    def run(self):
        print("STARTED!")

        def formater():
            directory = input("Путь к папке флагов: ")

            try:
                files = os.listdir(directory) #arr
            except:
                print(f"{Fore.RED}Ошибка! Неправильно указан путь.\n")
                formater()

            try:
                images = filter(lambda x: x.endswith('.tga'), files) 

                for name in images:
                    try:
                        flag = Image.open(f"{directory}\{name}")

                        flag = flag.resize((41, 26), Image.ANTIALIAS)
                        flag.save(f"{directory}\medium\{name}")

                        flag = flag.resize((10, 7), Image.ANTIALIAS)
                        flag.save(f"{directory}\small\{name}")

                        print(f"{Fore.GREEN}{name} отформатирован!")

                    except:
                        print(f"{Fore.RED}Ошибка при открытии или форматировании {name}")
                        try: errors+=1
                        except: errors=1
                print()

            except:
                print(f"{Fore.RED}Ошибка при считывании файлов!\n")
                formater()
            
            print(f"{Fore.GREEN}Флаги успешно отформатированы!")
            try: print(f"{Fore.RED}Всего {errors} ошибок при форматировании!")
            except: print(f"{Fore.GREEN}Нет ошибок при форматировании.")

            print()
            formater()
        
        formater()


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(313, 78)
        self.text_path = QtWidgets.QTextBrowser(Form)
        self.text_path.setGeometry(QtCore.QRect(40, 10, 261, 23))
        self.text_path.setObjectName("text_path")
        self.start = QtWidgets.QPushButton(Form)
        self.start.setGeometry(QtCore.QRect(80, 40, 181, 31))
        self.start.setObjectName("start")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(2, 60, 71, 20))
        self.label.setObjectName("label")
        self.but_path = QtWidgets.QPushButton(Form)
        self.but_path.setGeometry(QtCore.QRect(10, 10, 28, 23))
        self.but_path.setObjectName("but_path")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.frmtr = Formater(Form=self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Форматирование флагов"))
        self.start.setText(_translate("Form", "Пуск"))
        self.label.setText(_translate("Form", "by RubyRed"))
        self.but_path.setText(_translate("Form", "..."))


def app():
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    
    Form.show()

    ui.frmtr.start()

    sys.exit(app.exec_())
    
if __name__ == '__main__': app()