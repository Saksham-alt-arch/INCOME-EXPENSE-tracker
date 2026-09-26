import datetime
import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QPushButton)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

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
        self.top_label = QLabel("INCOME - EXPENSE - TRACKER\nTrack 🌻  Manage  🌻  Grow",self)
        self.top_label.setGeometry(250,0,300,45)
        self.top_label.setStyleSheet(
        "background-color: hsl(275, 8%, 28%);"
        "font-weight: bold;"
        "font-size: 18px;" 
        "color: hsl(176, 100%, 50%);" 
        "border: 1px solid;")
        self.top_label.setAlignment(Qt.AlignCenter)

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

        #Today's date display
        self.date_label = QLabel(f"Current date: {datetime.date.today()}",self)
        self.date_label.setGeometry(250,50,300,45)
        self.date_label.setStyleSheet("color: hsl(113, 100%, 50%);"
                                      "font-size: 19px;" 
                                      "font-weight: Bold;")

        #Account Summary Label
        self.acc_summary_label = QLabel("🧾 Account Summary",self)
        self.acc_summary_label.setGeometry(20,100,400,200)
        self.acc_summary_label.setStyleSheet("border: 3px solid;"
                                             "font-size: 19px;" 
                                             "font-weight: Bold;"
                                             "color: hsl(32, 100%, 50%);"
                                             "border-radius: 15px;")
        self.acc_summary_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        # Declaring Variables

        self.total_balance = 0
        self.total_income = 0
        self.total_expenses = 0
        float(self.total_balance)
        float(self.total_income)
        float(self.total_expenses)

        # Creating labels below the Account Summary Label

        self.total_balance_label = QLabel(f"Total Balance: $ {self.total_balance:,.2f}",self)
        self.total_balance_label.setGeometry(20,140,400,70)
        self.total_balance_label.setStyleSheet("color: hsl(153, 100%, 50%);"
                                               "border: 3px solid;" 
                                               "font-weight: Bold;" 
                                               "font-size: 23px;" 
                                               "border: 3px solid;")
        
        self.total_income = QLabel(f"Total Income: $ {self.total_income:,.2f}",self)
        self.total_income.setGeometry(26,202,390,47)
        self.total_income.setStyleSheet("color: hsl(113, 100%, 50%);"
                                        "font-weight: Bold;" 
                                        "font-size: 19px;")
        
        self.total_expenses = QLabel(f"Total Expenses: $ {self.total_expenses:,.2f}",self)
        self.total_expenses.setGeometry(26,245,390,50)
        self.total_expenses.setStyleSheet("color: hsl(0, 100%, 62%);" 
                                        "font-weight: Bold;" 
                                        "font-size: 19px;")

        # Creating the quick Actions Sections
        self.quick_action_label = QLabel("⚡ Quick Actions",self)
        self.quick_action_label.setGeometry(500,100,250,40)
        self.quick_action_label.setStyleSheet("font-size: 20px;" 
                                              "font-weight: Bold;" 
                                              "color: hsl(66, 100%, 50%)")
        self.quick_action_label.setAlignment(Qt.AlignCenter)

        # Creating Buttons
        self.income_button = QPushButton("➕ Add Income",self)
        self.income_button.setGeometry(500,150,250,40)
        self.expense_button = QPushButton("➖ Add Expense",self)
        self.expense_button.setGeometry(500,200,250,40)
        self.transactions_button = QPushButton("📂 View Transactions",self)
        self.transactions_button.setGeometry(500,250,250,40)

        self.income_button.setObjectName("income_button")
        self.expense_button.setObjectName("expense_button")
        self.transactions_button.setObjectName("transactions_button")

        # Setting CSS Styles to button

def main():
    app = QApplication(sys.argv)
    window = widget()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()