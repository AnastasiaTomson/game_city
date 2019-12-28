from PyQt5 import QtWidgets
from city import Ui_MainWindow
import sys
from game_cyti import *


class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        if self.ui.comp_city.text():
            last_letter = self.ui.comp_city.text()[-1]
        else:
            last_letter = ''
        res = check(city_list, self.ui.my_city.text().upper(), last_letter)
        self.ui.hint.setText(res['string'])
        if res['comp_city']:
            self.ui.comp_city.setText(res['comp_city'])
            self.ui.my_city.setText('')
        else:
            self.ui.my_city.setText('')


app = QtWidgets.QApplication([])
application = window()
application.show()
city_list = read()


sys.exit(app.exec())
