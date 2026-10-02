import mysql.connector
mydb = mysql.connector.connect(host = "LocalHost",
                                    user = "root",
                                    password = "MAHSKAS@Hell99",
                                    database = "income_expense_tracker")

def hello():
    print("Hello")