import datetime
import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QRadioButton, QHBoxLayout,
                            QLabel, QPushButton, QWidget, QLineEdit)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
        # Declaring Variables

    total_balance = 0
    total_income = 0
    total_expenses = 0
    float(total_balance)
    float(total_income)
    float(total_expenses)

    def __init__(self):
        super().__init__()
        self.incomeWindow = income_window()
        self.expenseWindow = expense_window()
        self.transactionsWindow = transaction_window()

        self.setWindowTitle("Income-Expense-Tracker")
        self.setWindowIcon(QIcon("INCOME-EXPENSE-tracker\\BankImage.jpg"))
        self.setGeometry(600,150,800,700)
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
                                      "font-weight: Bold;" 
                                      "text-decoration: underline;")

        #Account Summary Label
        self.acc_summary_label = QLabel("🧾 Account Summary",self)
        self.acc_summary_label.setGeometry(20,100,400,200)
        self.acc_summary_label.setStyleSheet("border: 2px solid;"
                                             "font-size: 19px;" 
                                             "font-weight: Bold;"
                                             "color: hsl(32, 100%, 50%);"
                                             "border-radius: 15px;")
        self.acc_summary_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        # Creating labels below the Account Summary Label

        self.total_balance_label = QLabel(f"Total Balance: $ {self.total_balance:,.2f}",self)
        self.total_balance_label.setGeometry(20,140,400,70)
        self.total_balance_label.setStyleSheet("color: hsl(153, 100%, 50%);"
                                               "font-weight: Bold;" 
                                               "font-size: 23px;"
                                               "border: 2px solid;")
        
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

        # Creating Buttons and adding CSS styles to them
        self.income_button = QPushButton("➕ Add Income",self)
        self.income_button.setGeometry(500,150,250,40)

        self.expense_button = QPushButton("➖ Add Expense",self)
        self.expense_button.setGeometry(500,200,250,40)

        self.transactions_button = QPushButton("📂 View Transactions",self)
        self.transactions_button.setGeometry(500,250,250,40)

        #Creating Object names for the buttons

        self.income_button.setObjectName("income_button")
        self.expense_button.setObjectName("expense_button")
        self.transactions_button.setObjectName("transactions_button")

        # Adding css styles to buttons and window
        self.setStyleSheet("""
            QMainWindow{background-color: hsl(176, 5%, 25%);}

            QPushButton{font-size: 19px;
            color: hsl(118, 0%, 99%);
            font-weight: Bold;
            border-radius: 15px;
            border: 1px solid;}

            QPushButton#income_button{background-color: hsl(118, 54%, 43%);}
            QPushButton#expense_button{background-color: hsl(0, 52%, 42%);}
            QPushButton#transactions_button{background-color: hsl(71, 52%, 42%);}

            QPushButton#income_button:hover{background-color: hsl(118, 54%, 55%);}
            QPushButton#expense_button:hover{background-color: hsl(0, 52%, 55%);}
            QPushButton#transactions_button:hover{background-color: hsl(71, 52%, 55%);}
        """)

        self.income_button.clicked.connect(self.add_income)
        self.expense_button.clicked.connect(self.add_expense)
        self.transactions_button.clicked.connect(self.view_transactions)

        # Creating functions for signal.connect(slot)

    def add_income(self):
        self.incomeWindow.show()

    def add_expense(self):
        self.expenseWindow.show()

    def view_transactions(self):
        self.transactionsWindow.show()
        
class income_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800,350,400,200)
        self.setWindowTitle("Add Income")
        self.setWindowIcon(QIcon("INCOME-EXPENSE-tracker\\BankImage.jpg"))

        self.income_description = QLineEdit()
        self.income_description.setPlaceholderText("Add income Description here")
        self.income_amount = QLineEdit()
        self.income_amount.setPlaceholderText("$ Add income Amount here")
        self.incomeButtonIW = QPushButton("Add Income",self)

        # Adding vertical layout manager to the income_window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        vbox = QVBoxLayout()
        vbox.addWidget(self.income_description)
        vbox.addWidget(self.income_amount)
        vbox.addWidget(self.incomeButtonIW)

        central_widget.setLayout(vbox)
        
        self.setStyleSheet("""
            QMainWindow{background-color: hsl(176, 5%, 25%);}
            QLineEdit{font-size: 20px;}
            QLineEdit:focus{background-color: hsl(217, 6%, 65%)}
            QPushButton{font-size: 20px;
                font-weight: Bold;
                border: 2px solid;
                padding: 15px 30px;
                border-radius: 25px;
                background-color: hsl(118, 54%, 43%);}
            QPushButton:hover{background-color: hsl(118, 54%, 55%);}
        """)

class expense_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(800,350,400,200)
        self.setWindowTitle("Add Expense")
        self.setWindowIcon(QIcon("INCOME-EXPENSE-tracker\\BankImage.jpg"))

        self.expense_description = QLineEdit()
        self.expense_description.setPlaceholderText("Add expense Description here")
        self.expense_amount = QLineEdit()
        self.expense_amount.setPlaceholderText("$ Add expense Amount here")
        self.expenseButtonEW = QPushButton("Add Expense",self)

        # Adding vertical layout manager to the expense_window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        vbox = QVBoxLayout()
        vbox.addWidget(self.expense_description)
        vbox.addWidget(self.expense_amount)
        vbox.addWidget(self.expenseButtonEW)
        
        central_widget.setLayout(vbox)

        self.setStyleSheet("""
            QMainWindow{background-color: hsl(176, 5%, 25%);}
            QLineEdit{font-size: 20px;}
            QLineEdit:focus{background-color: hsl(217, 6%, 65%)}
            QPushButton{font-size: 20px;
                font-weight: Bold;
                border: 2px solid;
                padding: 15px 30px;
                border-radius: 25px;
                background-color: hsl(0, 52%, 42%);}
            QPushButton:hover{background-color: hsl(0, 52%, 55%);}
        """)

class transaction_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600,300,800,500)
        self.setWindowTitle("View Transactions")
        self.setWindowIcon(QIcon("INCOME-EXPENSE-tracker\\BankImage.jpg"))

        self.month_Jan = QRadioButton("January", self)
        self.month_Feb = QRadioButton("February", self)
        self.month_Mar = QRadioButton("March", self)
        self.month_Apr = QRadioButton("April", self)
        self.month_May = QRadioButton("May", self)
        self.month_Jun = QRadioButton("June", self)
        self.month_Jul = QRadioButton("July", self)
        self.month_Aug = QRadioButton("August", self)
        self.month_Sep = QRadioButton("September", self)
        self.month_Oct = QRadioButton("October", self)
        self.month_Nov = QRadioButton("November", self)
        self.month_Dec = QRadioButton("December", self)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        vbox = QVBoxLayout()
        vbox.addWidget(self.month_Jan)
        vbox.addWidget(self.month_Feb)
        vbox.addWidget(self.month_Mar)
        vbox.addWidget(self.month_Apr)
        vbox.addWidget(self.month_May)
        vbox.addWidget(self.month_Jun)
        vbox.addWidget(self.month_Jul)
        vbox.addWidget(self.month_Aug)
        vbox.addWidget(self.month_Sep)
        vbox.addWidget(self.month_Oct)
        vbox.addWidget(self.month_Nov)
        vbox.addWidget(self.month_Dec)

        central_widget.setLayout(vbox)

        self.setStyleSheet("""
            QMainWindow{background-color: hsl(176, 5%, 25%);}
            QRadioButton{color: hsl(182, 100%, 50%);
                        font-size: 20px;}
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()