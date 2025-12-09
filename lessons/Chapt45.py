# PyQt5 Labels
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt #used for alignments

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lets learn Labels")
        self.setGeometry( 700, 300, 500, 500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline")
        
        # label.setAlignment(Qt.AlignTop) #Vertically top align
        # label.setAlignment(Qt.AlignBottom) #Vertically bottom align
        # label.setAlignment(Qt.AlignVCenter) #Vertically center align

        # label.setAlignment(Qt.AlignRight) #Horizontally right align
        # label.setAlignment(Qt.AlignLeft) #Horizontally left align
        # label.setAlignment(Qt.AlignHCenter) #Horizontally center align

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #Center and Top
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) #Center and Bottom
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #Center and Center
        label.setAlignment(Qt.AlignCenter) #Center and Center

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()