from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.lastPressed = False
        self.label = QLabel()

        self.button1 = QPushButton("1")
        self.button1.clicked.connect(self.button1_clicked)
        self.button2 = QPushButton("2")
        self.button2.clicked.connect(self.button2_clicked)
        self.button3 = QPushButton("3")
        self.button3.clicked.connect(self.button3_clicked)
        self.button4 = QPushButton("4")
        self.button4.clicked.connect(self.button4_clicked)
        self.button5 = QPushButton("5")
        self.button5.clicked.connect(self.button5_clicked)
        self.button6 = QPushButton("6")
        self.button6.clicked.connect(self.button6_clicked)
        self.button7 = QPushButton("7")
        self.button7.clicked.connect(self.button7_clicked)
        self.button8 = QPushButton("8")
        self.button8.clicked.connect(self.button8_clicked)
        self.button9 = QPushButton("9")
        self.button9.clicked.connect(self.button9_clicked)
        self.button_plus = QPushButton("+")
        self.button_plus.clicked.connect(self.button_plus_clicked)
        self.button_minus = QPushButton("-")
        self.button_minus.clicked.connect(self.button_minus_clicked)
        self.button_multiply = QPushButton("*")
        self.button_multiply.clicked.connect(self.button_multiply_clicked)
        self.button_divide = QPushButton("/")
        self.button_divide.clicked.connect(self.button_divide_clicked)
        self.button_even = QPushButton("=")
        self.button_even.clicked.connect(self.button_divide_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button1, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.button2, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.button3, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        layout.addWidget(self.button6)
        layout.addWidget(self.button7)
        layout.addWidget(self.button8)
        layout.addWidget(self.button9)
        layout.addWidget(self.button_plus)
        layout.addWidget(self.button_minus)
        layout.addWidget(self.button_multiply)
        layout.addWidget(self.button_divide)
        layout.addWidget(self.button_even)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.setFixedSize(400, 600)

    def button1_clicked(self):
        if not self.lastPressed:
            self.label.setText(self.label.text() + " 1")
            self.lastPressed = True
        else:
            self.label.setText(self.label.text() + "1")

    def button2_clicked(self):
        if not self.lastPressed:
            self.label.setText(self.label.text() + " 2")
            self.lastPressed = True
        else:
            self.label.setText(self.label.text() + "2")

    def button3_clicked(self):
        if not self.lastPressed:
            self.label.setText(self.label.text() + " 3")
            self.lastPressed = True
        else:
            self.label.setText(self.label.text() + "3")

    def button4_clicked(self):
        if not self.lastPressed:
            self.label.setText(self.label.text() + " 4")
            self.lastPressed = True
        else:
            self.label.setText(self.label.text() + "4")

    def button5_clicked(self):
        if not self.lastPressed:
            self.label.setText(self.label.text() + " 5")
            self.lastPressed = True
        else:
            self.label.setText(self.label.text() + "5")

    def button6_clicked(self):
        if not self.lastPressed:
            self.label.setText(self.label.text() + " 6")
            self.lastPressed = True
        else:
            self.label.setText(self.label.text() + "6")

    def button7_clicked(self):
        if not self.lastPressed:
            self.label.setText(self.label.text() + " 7")
            self.lastPressed = True
        else:
            self.label.setText(self.label.text() + "7")

    def button8_clicked(self):
        if not self.lastPressed:
            self.label.setText(self.label.text() + " 8")
            self.lastPressed = True
        else:
            self.label.setText(self.label.text() + "8")

    def button9_clicked(self):
        if not self.lastPressed:
            self.label.setText(self.label.text() + " 9")
            self.lastPressed = True
        else:
            self.label.setText(self.label.text() + "9")

    def button_plus_clicked(self):
        if self.lastPressed:
            self.label.setText(self.label.text() + " +")
            self.lastPressed = False

    def button_minus_clicked(self):
        if self.lastPressed:
            self.label.setText(self.label.text() + " -")
            self.lastPressed = False

    def button_multiply_clicked(self):
        if self.lastPressed:
            self.label.setText(self.label.text() + " *")
            self.lastPressed = False

    def button_divide_clicked(self):
        if self.lastPressed:
            self.label.setText(self.label.text() + " /")
            self.lastPressed = False

    def button_even_clicked(self):
        self.label.setText(calculate(self))
        
    def calculate(self, equation: str) -> str:
        pass

    def toNumbers(equation: str):
        equation_elements: list[str] = equation.split(" ")
        if not (equation_elements[0].isnumeric() and equation_elements[len(equation_elements) - 1]):
            self.label.setText("Incorrect input")
            return None
        equation_elements_transformed = []
        for element in equation_elements:
            try:
                equation_elements_transformed.append(int(element))
            except ValueError:
                equation_elements_transformed.append(element)
        return equation_elements_transformed
    

app = QApplication([])
window = MainWindow()
window.show()

app.exec()
