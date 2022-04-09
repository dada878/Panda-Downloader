from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import re
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

window = tk.Tk()
window.withdraw()

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(280, 130)
        Form.setMaximumSize(QtCore.QSize(280, 130))
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 261, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 70, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.download)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def download(self):
        
        try:
            root = requests.get(self.lineEdit.text()).text
            link = re.findall('<source src="(.+)" type="audio\/mpeg">',root)[0]
            mp3 = requests.get("https:"+link).content
        except:
            messagebox.showerror("錯誤", "錯誤的連結")
            return

        try:
            messagebox.showinfo("提示","音檔抓取成功，請選擇存檔位置")
            file = filedialog.asksaveasfile(filetypes=[("音訊檔案", "*.mp3")],mode="wb",defaultextension=".mp3")
            file.write(mp3)
            file.close()
            messagebox.showinfo("提示","下載成功！")
        except:
            messagebox.showinfo("提示","未選擇檔案位置")
            return

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "熊貓辦公音效下載破解"))
        self.label.setText(_translate("Form", "貼上連結："))
        self.pushButton.setText(_translate("Form", "開始下載"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
