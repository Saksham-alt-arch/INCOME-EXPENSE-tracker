import datetime
import sys
from Sqlconnect import mydb
from PyQt5.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QRadioButton,
                            QLabel, QPushButton, QWidget, QLineEdit)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
                    
    def __init__(self):
        super().__init__()
        self.incomeWindow = income_window()
        self.expenseWindow = expense_window()
        self.transactionsWindow = transaction_window()
        self.setWindowTitle("Income-Expense-Tracker")
        self.setWindowIcon(QIcon("INCOME-EXPENSE-tracker\\BankImage.jpg"))
        self.setGeometry(600,150,800,550)
        self.initUI()

    # Declaring Variables and setting functions
    def total_balance(self):
        sql_balance = "SELECT Balance FROM total_balance;"
        my_cursor = mydb.cursor()
        my_cursor.execute(sql_balance)
        total_balances = my_cursor.fetchone()
        for output in total_balances:
            total_balance = output
            return total_balance

    def total_income_(self):
        sql_income = "SELECT amount FROM total_income;"
        my_cursor = mydb.cursor()
        my_cursor.execute(sql_income)
        total_incomes = my_cursor.fetchone()
        for output_inc in total_incomes:
            total_income = output_inc
            return total_income

    def total_expense(self):     
        sql_expense = "SELECT amount FROM total_expense;"
        my_cursor = mydb.cursor()
        my_cursor.execute(sql_expense)
        total_expenses = my_cursor.fetchone()
        for output_exp in total_expenses:
            total_expense = output_exp
            return total_expense

    def output(self):
        # Showing 5 most recent transactions
        my_cursor = mydb.cursor()
        sql = "SELECT Date_, Description_, Type_, Amount_ " \
        "FROM transactions ORDER BY ID DESC LIMIT 5;"

        my_cursor.execute(sql)
        results = my_cursor.fetchall()
        output = ""
        for result in results:
            output += "\n"
            for index, individual in enumerate(result):
                    if index == 0:
                        output += f"{individual}"
                    elif index == 1:
                        output += f"\t{individual:<25}"
                    elif index == 2:
                        output += f"   {individual}"
                    elif index == 3:
                        output += f"   {individual:>10}"
                    else: 
                        pass
        return output

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
        self.total_balance_label = QLabel(f"Total Balance: $ {self.total_balance()}",self)
        self.total_balance_label.setGeometry(20,140,400,70)
        self.total_balance_label.setStyleSheet("color: hsl(153, 100%, 50%);"
                                               "font-weight: Bold;" 
                                               "font-size: 23px;"
                                               "border: 2px solid;")
        
        self.total_income = QLabel(f"Total Income: $ {self.total_income_()}",self)
        self.total_income.setGeometry(26,202,390,47)
        self.total_income.setStyleSheet("color: hsl(113, 100%, 50%);"
                                        "font-weight: Bold;" 
                                        "font-size: 19px;")
        
        self.total_expenses = QLabel(f"Total Expenses: $ {self.total_expense()}",self)
        self.total_expenses.setGeometry(26,245,390,50)
        self.total_expenses.setStyleSheet("color: hsl(0, 100%, 62%);" 
                                        "font-weight: Bold;" 
                                        "font-size: 19px;")

        self.recent5tranactions = QLabel("Recent 5 Transactions 📇",self)
        self.recent5tranactions.setGeometry(26,305,270,50)
        self.recent5tranactions.setStyleSheet("font-weight: Bold;"
                                              "font-size: 20px;"
                                              "color: hsl(198, 100%, 81%);")

        self.transactions5 = QLabel(self)
        self.transactions5.setGeometry(26,370,750,175)
        self.transactions5.setStyleSheet("font-size: 20px;"
                                         "color: hsl(239, 100%, 90%);" \
                                         "font-family: Consolas;")
        
        self.transactions5.setAlignment(Qt.AlignTop)

        self.recent5description = QLabel("     DATE\t\tDESCRIPTION \t\t    TYPE  \t      $AMOUNT",self)
        self.recent5description.setGeometry(26,345,750,50)
        self.recent5description.setStyleSheet("font-weight: Bold;"
                                               "font-size: 20px;"
                                                "color: hsl(54, 100%, 50%);")
        self.recent5tranactions.setAlignment(Qt.AlignCenter)
        self.transactions5.setText(self.output())

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
        self.incomeWindow.incomeButtonIW.setDisabled(False)
        self.incomeWindow.incomeButtonIW.setText("Add Income")
        self.incomeWindow.income_description.clear()
        self.incomeWindow.income_amount.clear()
        self.incomeWindow.error_label.setText("*********** NO  ERRORS **********")
        self.incomeWindow.error_label.setStyleSheet("color: Black;" \
                            "font-weight: Normal;")
        self.incomeWindow.show()

    def add_expense(self):
        self.expenseWindow.expenseButtonEW.setDisabled(False)
        self.expenseWindow.expenseButtonEW.setText("Add Expense")
        self.expenseWindow.expense_description.clear()
        self.expenseWindow.expense_amount.clear()
        self.expenseWindow.error_label.setText("*********** NO  ERRORS **********")
        self.expenseWindow.error_label.setStyleSheet("color: Black;" \
                            "font-weight: Normal;")
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
            self.error_label = QLabel("*********** NO  ERRORS **********",self)
            self.error_label.setAlignment(Qt.AlignCenter)
            self.incomeButtonIW = QPushButton("Add Income",self)

            # Adding vertical layout manager to the income_window
            central_widget = QWidget()
            self.setCentralWidget(central_widget)
            vbox = QVBoxLayout()
            vbox.addWidget(self.income_description)
            vbox.addWidget(self.income_amount)
            vbox.addWidget(self.error_label)
            vbox.addWidget(self.incomeButtonIW)

            central_widget.setLayout(vbox)
            
            self.setStyleSheet("""
                QMainWindow{background-color: hsl(176, 5%, 25%);}
                QLineEdit{font-size: 20px;}
                QLineEdit:focus{background-color: hsl(217, 6%, 65%)}
                QLabel{font-size: 20px;}
                QPushButton{font-size: 20px;
                    font-weight: Bold;
                    border: 2px solid;
                    padding: 15px 30px;
                    border-radius: 25px;
                    background-color: hsl(118, 54%, 43%);}
                QPushButton:hover{background-color: hsl(118, 54%, 55%);}
            """)

            self.incomeButtonIW.clicked.connect(self.income_sql)

        def income_sql(self):
            desc = self.income_description.text()
            amt = self.income_amount.text()

            try:
                if len(desc) < 3:
                    self.error_label.setText("Error: Make Description > 3 chars!")
                    self.error_label.setStyleSheet("color: hsl(0, 100%, 62%);" \
                                "font-weight: Bold;")

                elif len(amt) == 0:
                    self.error_label.setText("Error: Please enter an amount!")
                    self.error_label.setStyleSheet("color: hsl(0, 100%, 62%);" \
                                "font-weight: Bold;")

                elif float(amt) == 0:
                    self.error_label.setText("Error: Income cannot be zero!")
                    self.error_label.setStyleSheet("color: hsl(0, 100%, 62%);" \
                                    "font-weight: Bold;")

                else:
                    self.error_label.setText("*********** NO  ERRORS **********")
                    self.error_label.setStyleSheet("color: Black;" \
                    "font-weight: Normal;")

                    my_cursor = mydb.cursor()
                    sql = "INSERT INTO transactions(Date_,Description_,Type_,Amount_) " \
                                "VALUES(CURRENT_DATE(),%s,%s,%s);"
                    values = (desc,"Income",amt)

                    my_cursor.execute(sql,values)
                    mydb.commit()

                    self.incomeButtonIW.setText("Income Added!")
                    self.incomeButtonIW.setDisabled(True)
                    self.incomeButtonIW.setStyleSheet("color: Black;")

            except ValueError:
                self.error_label.setText("Error: Enter a Float or Int number!")
                self.error_label.setStyleSheet("color: hsl(0, 100%, 62%);" \
                                                "font-weight: Bold;")
                
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
        self.error_label = QLabel("*********** NO  ERRORS **********",self)
        self.error_label.setAlignment(Qt.AlignCenter)
        self.expenseButtonEW = QPushButton("Add Expense",self)

        # Adding vertical layout manager to the expense_window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        vbox = QVBoxLayout()
        vbox.addWidget(self.expense_description)
        vbox.addWidget(self.expense_amount)
        vbox.addWidget(self.error_label)
        vbox.addWidget(self.expenseButtonEW)
        
        central_widget.setLayout(vbox)

        self.setStyleSheet("""
            QMainWindow{background-color: hsl(176, 5%, 25%);}
            QLineEdit{font-size: 20px;}
            QLineEdit:focus{background-color: hsl(217, 6%, 65%)}
            QLabel{font-size: 20px;}
            QPushButton{font-size: 20px;
                font-weight: Bold;
                border: 2px solid;
                padding: 15px 30px;
                border-radius: 25px;
                background-color: hsl(0, 52%, 42%);}
            QPushButton:hover{background-color: hsl(0, 52%, 55%);}
        """)

        self.expenseButtonEW.clicked.connect(self.expense_sql)

    def expense_sql(self):
            desc = self.expense_description.text()
            amt = self.expense_amount.text()
    
            try:
                if len(desc) < 3:
                    self.error_label.setText("Error: Make Description > 3 chars!")
                    self.error_label.setStyleSheet("color: hsl(0, 100%, 62%);" \
                                "font-weight: Bold;")
    
                elif len(amt) == 0:
                    self.error_label.setText("Error: Please enter an amount!")
                    self.error_label.setStyleSheet("color: hsl(0, 100%, 62%);" \
                                "font-weight: Bold;")
    
                elif float(amt) == 0:
                    self.error_label.setText("Error: Expense cannot be zero!")
                    self.error_label.setStyleSheet("color: hsl(0, 100%, 62%);" \
                                    "font-weight: Bold;")
    
                else:
                    self.error_label.setText("*********** NO  ERRORS **********")
                    self.error_label.setStyleSheet("color: Black;" \
                    "font-weight: Normal;")
    
                    my_cursor = mydb.cursor()
                    sql = "INSERT INTO transactions(Date_,Description_,Type_,Amount_) " \
                                "VALUES(CURRENT_DATE(),%s,%s,-%s);"
                    values = (desc,"Expense",amt)
    
                    my_cursor.execute(sql,values)
                    mydb.commit()
    
                    self.expenseButtonEW.setText("Expense Added!")
                    self.expenseButtonEW.setDisabled(True)
                    self.expenseButtonEW.setStyleSheet("color: Black;")
    
            except ValueError:
                self.error_label.setText("Error: Enter a Float or Int number!")
                self.error_label.setStyleSheet("color: hsl(0, 100%, 62%);" \
                                                "font-weight: Bold;")

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