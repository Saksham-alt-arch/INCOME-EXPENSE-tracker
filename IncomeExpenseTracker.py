import datetime
import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel,
                             QHBoxLayout,QVBoxLayout)
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QTime

class widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Income-Expense-Tracker")
        self.setWindowIcon(QIcon("INCOME-EXPENSE-tracker\\BankImage.jpg"))
        self.setGeometry(600,150,800,700)
        self.setStyleSheet("background-color: hsl(176, 5%, 25%);")
        self.initUI()

    def initUI(self):
        # Top label
        self.top_label = QLabel("INCOME - EXPENSE - TRACKER\nTrack *  Manage  *  Grow",self)
        self.top_label.setGeometry(250,0,300,45)
        self.top_label.setStyleSheet(
        "background-color: hsl(275, 8%, 28%);"
        "font-weight: bold;"
        "font-size: 18px;" 
        "color: hsl(176, 100%, 50%);" 
        "border: 1px solid;")
        self.top_label.setAlignment(Qt.AlignCenter)

        #Today's date display
        self.date_label = QLabel(f"Current date: {datetime.date.today()}",self)
        self.date_label.setGeometry(250,50,300,45)
        self.date_label.setStyleSheet("color: hsl(113, 100%, 50%);"
                                      "font-size: 19px;" 
                                      "font-weight: Bold;")

        # Top Image to go with the top label
        self.image = QPixmap("INCOME-EXPENSE-tracker\\BankImage.jpg")
        self.bank_pic = QLabel(self)
        self.bank_pic.setPixmap(self.image)
        self.bank_pic.setStyleSheet(
        "font: 20px;" 
        "border:3px solid;" 
        "border-radius: 10px;")
        self.bank_pic.setScaledContents(True)
        self.bank_pic.setGeometry(210,0,40,45)
"""
        # Layouts
        central_widget = QWidget()
        vbox = QVBoxLayout()
        vbox.addWidget(self.top_label)
        vbox.addWidget(self.date_label)
        central_widget.setLayout(vbox)
"""

def main():
    app = QApplication(sys.argv)
    window = widget()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()