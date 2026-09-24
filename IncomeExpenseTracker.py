import sys
from PyQt5.QtWidgets import QWidget, QApplication

class widget(QWidget):
    def __init__(self):
        super().__init__()

def main():
    app = QApplication(sys.argv)
    window = widget()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()