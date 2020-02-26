import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class RPS_game(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setWindowTitle("RPS Game")
        self.setGeometry(350,200,600,300)


        #labels and buttons
        self.info = QLabel("Please press PLAY button to play.")
        self.label1 = QLabel()
        self.label2 = QLabel()
        self.btn_play = QPushButton("PLAY")
        self.num1 = QLabel()
        self.num2 = QLabel()
        self.list = ["rock.png", "paper.png", "scissor.png"]
        self.n1 = 0
        self.n2 = 0

        #labels decoration
        self.info.setAlignment(Qt.AlignCenter)
        self.info.setFont(QFont("Arial", 12))
        self.label1.setPixmap(QPixmap("question.png"))
        self.label2.setPixmap(QPixmap("question.png"))
        self.label1.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter)
        self.num1.setAlignment(Qt.AlignCenter)
        self.num2.setAlignment(Qt.AlignCenter)
        self.num1.setFont(QFont("Arial", 14))
        self.num2.setFont(QFont("Arial", 14))




        #layouts
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        vbox.addWidget(self.info)
        hbox1.addWidget(self.label1)
        hbox1.addWidget(self.label2)
        hbox2.addWidget(self.num1)
        hbox2.addWidget(self.num2)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.btn_play)
        self.setLayout(vbox)


        self.btn_play.clicked.connect(self.play)

        self.show()


    #play function
    def play(self):
        random1 = random.choice(self.list)
        random2 = random.choice(self.list)
        self.label1.setPixmap(QPixmap(random1))
        self.label2.setPixmap(QPixmap(random2))
        print(random1)
        print(random2)


        self.num1.setText(str(self.n1))
        self.num2.setText(str(self.n2))
        print( self.n1 )
        print( self.n2 )
        if random1 == "rock.png" and random2 == "scissor.png":
            self.n1 += 1
        elif random1 == "rock.png" and random2 == "paper.png":
            self.n2 += 1
        elif random1 == "paper.png" and random2 == "rock.png":
            self.n1 += 1
        elif random1 == "paper.png" and random2 == "scissor.png":
            self.n2 += 1
        elif random1 == "scissor.png" and random2 == "paper.png":
            self.n1 += 1
        elif random1 == "scissor.png" and random2 == "rock.png":
            self.n2 += 1


app = QApplication(sys.argv)
rps_game = RPS_game()
sys.exit(app.exec_())
    