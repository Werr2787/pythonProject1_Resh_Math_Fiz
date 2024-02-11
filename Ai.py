import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QPushButton, QLabel, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.spin_box = QSpinBox()
        self.button = QPushButton('Output Spin Box Value')
        self.label = QLabel('Spin Box Value:')

        self.button.clicked.connect(self.output_spin_box_value)

        layout = QVBoxLayout()
        layout.addWidget(self.spin_box)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.setWindowTitle('Spin Box Example')
        self.show()

    def output_spin_box_value(self):
        value = self.spin_box.value()
        self.label.setText(f'Spin Box Value: {value}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())