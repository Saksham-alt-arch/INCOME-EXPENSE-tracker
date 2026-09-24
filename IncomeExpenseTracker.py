import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Income-Expense-Tracker")
        self.setWindowIcon(QIcon("INCOME-EXPENSE-tracker\\BankImage.jpg"))
        self.setGeometry(600,150,800,700)
        self.initUI()

    def initUI(self):
        # Top label
        self.top_label = QLabel("INCOME-EXPENSE-TRACKER",self)
        self.top_label.setGeometry(0,0,799,50)

        # Top Image to go with the top label
        self.image = QPixmap("INCOME-EXPENSE-tracker\\BankImage.jpg")
        self.bank_pic = QLabel(self)
        self.bank_pic.setPixmap(self.image)
        self.bank_pic.setGeometry(0,0,75,50)
        self.bank_pic.setScaledContents(True)

        # Setting CSS styles
        self.setStyleSheet("""
                background-color: hsl(275, 8%, 28%);
            top_label{
                    font_size: 40px;
            }
        """
        )
        print("Hello")

def main():
    app = QApplication(sys.argv)
    window = widget()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()