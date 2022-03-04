from time import sleep
from serial import *
import sys
from gui import *
import os
import shutil
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog
)


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.connect_to_device())
        self.ui.pushButton_2.clicked.connect(lambda: self.load_data_from_device())
        self.ui.save.clicked.connect(lambda: self.saveFileDialog())
        self.stop_reading = False

        self.ui.parity.addItems(['PARITY_ODD','PARITY_NONE','PARITY_EVEN', 'PARITY_MARK', 'PARITY_SPACE'])
        self.ui.stopbits.addItems(['STOPBITS_TWO', 'STOPBITS_ONE','STOPBITS_ONE_POINT_FIVE'])
        self.ui.bytesize.addItems(['SEVENBITS', 'FIVEBITS','SIXBITS', 'EIGHTBITS'])
        self.ui.baudrate.addItems(['9600','50', '75', '110', '134', '150', '200', '300', '600',
                                   '1200', '1800', '2400', '4800',  '19200', '38400', '57600', '115200'])
        #self.ui.com.addItems(['COM1', 'COM2', 'COM3', 'COM4','COM5'])

        self.filename = "Wyniki.txt"
        self.is_save = False

        self.options = {
            "PARITY_NONE": PARITY_NONE,
            "PARITY_EVEN": PARITY_EVEN,
            "PARITY_ODD": PARITY_EVEN,
            'PARITY_MARK' : PARITY_MARK,
            'PARITY_SPACE' : PARITY_SPACE,
            'STOPBITS_ONE' : STOPBITS_ONE,
            'STOPBITS_ONE_POINT_FIVE' : STOPBITS_ONE_POINT_FIVE,
            'STOPBITS_TWO' : STOPBITS_TWO,
            'FIVEBITS' : FIVEBITS,
            'SIXBITS' : SIXBITS,
            'SEVENBITS' : SEVENBITS,
            'EIGHTBITS' : EIGHTBITS
            # i tak dalej..
        }

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "Text Files (*.txt)", options=options)



        #self.filename = fileName
        self.is_save = True
        f = open(fileName +'.txt', 'w')
        print(fileName+'.txt', '    ',self.filename)
        shutil.copyfile(self.filename, fileName+'.txt')
        # open both files

        os.remove(self.filename)


    def connect_to_device(self):
        self.stop_reading = True



    def load_data_from_device(self):
        self.stop_reading = False

        for i in range(1,11):
            try:
                prt = 'COM' + str(i)
                ser = Serial(
                port=prt,
                baudrate=int(self.ui.baudrate.currentText()),
                timeout=1,
                parity=self.options[self.ui.parity.currentText()],
                stopbits=self.options[self.ui.stopbits.currentText()],
                bytesize=self.options[self.ui.bytesize.currentText()]
                            )
                ser.isOpen()
            except:
                continue
            text = ''
        while True:
            if  self.stop_reading:
                break
            i += 1
            #text += str(i)
            #text += '\n'
            #print(i)

            bytesToRead = ser.inWaiting()
            data = ser.read(bytesToRead)
            sleep(0.5)
            data = (data.decode(encoding='utf-8', errors='strict'))

            QtCore.QCoreApplication.processEvents()
            try:
                with open(self.filename, "a") as file:
                    QtCore.QCoreApplication.processEvents()
                    file.write(data)
                    #file.write('sakra')
                file.close()

                f = open(self.filename, 'r')
                file_contents = f.read()
                text = file_contents
                self.ui.textBrowser.setText(text)
                f.close()

                #print(self.filename)

                if self.is_save:
                    #os.remove("Odczyty_buffor.txt")
                    self.ui.textBrowser.setText('')
                    self.is_save = False

            except Exception as e:
                print(e)



# ser = Serial(
#     port='COM3',
#     baudrate=9600,
#     timeout=1,
#     parity=PARITY_ODD,
#     stopbits=STOPBITS_TWO,
#     bytesize=SEVENBITS
# )
# ser.isOpen()

# while True:
#     bytesToRead = ser.inWaiting()
#     data = ser.read(bytesToRead)
#     sleep(1)
#     data = (data.decode(encoding='utf-8', errors='strict'))
#     print(data)
#     #text += str(data, 'utf-8', 'replace')
#     #self.ui.textBrowser.setText(self.text)
#     with open("Odczyty.txt", "a") as file:
#         file.write(data)

def main():
    try:
        app = QApplication(sys.argv)
        win = Window()
        win.show()
        sys.exit(app.exec())

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()


