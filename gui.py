import sys
from PyQt5.QtGui import QColor,QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import requests



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the UI elements
        self.text_box = QLineEdit()
        self.predict_button = QPushButton('Predict')
        self.result_label = QLabel()

        # Set up the layout
        layout = QVBoxLayout()
        label = QLabel('Enter text to classify:')
        label.setFont(QFont('Times New Roman',20))
        layout.addWidget(label)
        layout.addWidget(self.text_box)
        layout.addWidget(self.predict_button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

        # Connect the predict_button to the predict function
        self.predict_button.clicked.connect(self.predict)

    def predict(self):
        # Get the text input from the text_box
        text = self.text_box.text()

        # Send a POST request to your API
        url = 'http://127.0.0.1:5000/predict'
        data = {'text': text}
        response = requests.post(url, json=data)

        # Display the prediction result
        if response.status_code == 200:
            result = response.json()['prediction']
            self.result_label.setText(f'Prediction: {result}')
        else:
            QMessageBox.critical(self, 'Error', 'Failed to get prediction.')

if __name__ == '__main__':
    # Create the application and main window
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet("background-color: lightblue;")
    # Show the window and start the event loop
    window.show()
    sys.exit(app.exec_())
