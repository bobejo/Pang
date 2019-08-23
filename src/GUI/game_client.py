import sys
import logging
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QDialog
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.uic import loadUi


class ChooseStart(QDialog):
    def __init__(self):
        super(ChooseStart, self).__init__()
        loadUi('choose_start.ui', self)
        self.setFixedSize(self.size())
        self.setWindowTitle('Pang Game')
        self.pushButton.clicked.connect(self.start_host)
        self.pushButton_2.clicked.connect(self.start_client)

    @pyqtSlot()
    def start_host(self):
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        logging.info('Hosting game')
        print("Hosting game")

    @pyqtSlot()
    def start_client(self):
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.close()
        logging.info('Joining game')
        print("Starting Client")
        widget = ClientStart()
        widget.show()
        widget.exec_()


class ClientStart(QDialog):
    def __init__(self):
        super(ClientStart, self).__init__()
        loadUi('client_start.ui', self)
        self.setFixedSize(self.size())
        self.setWindowTitle('Join server')
        self.pushButton.clicked.connect(self.join_server)

    @pyqtSlot()
    def join_server(self):
        self.pushButton.setEnabled(False)
        print('Joining server on IP {} with username {}'.format(self.lineEdit.text(), self.lineEdit_2.text()))
        main_window = ClientGame()
        main_window.show()
        main_window.exec_()
        self.close()


class ClientGame(QMainWindow):
    def __init__(self):
        super(ClientGame, self).__init__()
        loadUi('client_game.ui', self)
        self.setFixedSize(self.size())
        self.setWindowTitle('Pang Game')
        self.lineEdit.returnPressed.connect(self.send_command)
        self.textEdit.insertPlainText('Game loaded\n')


    @pyqtSlot()
    def send_command(self):
        if self.lineEdit.text():
            print('Sent command: {}'.format(self.lineEdit.text()))
            self.textEdit.insertPlainText('Sent command: {} \n'.format(self.lineEdit.text()))
            self.lineEdit.clear()



app = QApplication(sys.argv)
widget = ChooseStart()
#widget = ClientGame()
widget.show()
app.exec_()