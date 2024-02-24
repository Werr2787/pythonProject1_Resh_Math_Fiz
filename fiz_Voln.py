import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
import requests
from io import BytesIO
from PIL import Image

class PhotoChecker(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.label = QLabel(self)
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Photo Checker')

    def check_photo(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Проверяем, был ли успешный HTTP-код ответа

            # Пытаемся открыть изображение с помощью Pillow
            image = Image.open(BytesIO(response.content))
            image.verify()  # Проверяем целостность файла изображения

            # Отображаем изображение в QLabel
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            self.label.setPixmap(pixmap)
            self.label.show()

            print("Ссылка на фото действительна и ведет к изображению.")
        except Exception as e:
            print(f"Ошибка при проверке ссылки на фото: {e}")
            self.label.clear()
            self.label.setText("Невозможно загрузить фото по указанной ссылке.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    photo_checker = PhotoChecker()
    photo_checker.show()

    # Замените URL ниже на тот, который вы хотите проверить
    photo_checker.check_photo("D:/Downloads/Rech_Math_Fiz/Photos/Снимок экрана 2024-02-10 182600.png")

    sys.exit(app.exec_())

