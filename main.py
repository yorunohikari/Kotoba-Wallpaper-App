import sys
import json
import random
import threading
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QColorDialog, QSpinBox
from PyQt5.QtCore import QTimer
from generate_image import load_vocab_from_json, generate_image
from change_wallpaper import change_wallpaper
import pystray
from pystray import MenuItem as item
from PIL import Image as PilImage

class WallpaperApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.vocab_file = os.path.abspath("data/vocab.json")
        self.output_image = os.path.abspath("backgrounds/japstudy_bg.jpg")
        self.interval = 3600  # default interval in seconds (1 hour)
        self.text_color = "black"
        self.bg_color = "white"
        self.vocab_list = load_vocab_from_json(self.vocab_file)

        self.initUI()
        self.tray_icon = None
        self.create_tray_icon()

        # Initialize timers
        self.timer = QTimer(self)
        self.countdown_timer = QTimer(self)
        self.time_left = self.interval

        self.start_wallpaper_update()

    def initUI(self):
        self.setWindowTitle('Japanese Wallpaper App')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.countdown_label = QLabel('Next update in: 00:00:00', self)
        layout.addWidget(self.countdown_label)

        self.interval_label = QLabel('Update Interval (seconds):', self)
        layout.addWidget(self.interval_label)
        
        self.interval_spinbox = QSpinBox(self)
        self.interval_spinbox.setMinimum(60)
        self.interval_spinbox.setMaximum(86400)
        self.interval_spinbox.setValue(self.interval)
        layout.addWidget(self.interval_spinbox)
        
        self.text_color_button = QPushButton('Choose Text Color', self)
        self.text_color_button.clicked.connect(self.choose_text_color)
        layout.addWidget(self.text_color_button)
        
        self.bg_color_button = QPushButton('Choose Background Color', self)
        self.bg_color_button.clicked.connect(self.choose_bg_color)
        layout.addWidget(self.bg_color_button)
        
        self.update_button = QPushButton('Update Now', self)
        self.update_button.clicked.connect(self.update_wallpaper)
        layout.addWidget(self.update_button)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def choose_text_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_color = color.name()

    def choose_bg_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.bg_color = color.name()

    def update_wallpaper(self):
        vocab = random.choice(self.vocab_list)
        generate_image(vocab, self.output_image, text_color=self.text_color, bg_color=self.bg_color)
        print(f"Generated wallpaper at {self.output_image}")  # Debugging info
        change_wallpaper(self.output_image)
        print(f"Changed wallpaper to {self.output_image}")  # Debugging info
        self.reset_countdown_timer()

    def start_wallpaper_update(self):
        self.update_wallpaper()
        self.timer.timeout.connect(self.update_wallpaper)
        self.timer.start(self.interval * 1000)
        
        self.countdown_timer.timeout.connect(self.update_countdown)
        self.countdown_timer.start(1000)  # Update every second

    def reset_countdown_timer(self):
        self.time_left = self.interval
        self.update_countdown()

    def update_countdown(self):
        self.time_left -= 1
        if self.time_left <= 0:
            self.time_left = 0

        hours, remainder = divmod(self.time_left, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.countdown_label.setText(f'Next update in: {hours:02}:{minutes:02}:{seconds:02}')

    def create_tray_icon(self):
        image = PilImage.open("icon.png")  # Path to your icon image
        menu = (item('Show', self.show_app), item('Quit', self.quit_app))
        self.tray_icon = pystray.Icon("WallpaperApp", image, "Japanese Wallpaper App", menu)
        threading.Thread(target=self.tray_icon.run).start()

    def show_app(self):
        self.show()

    def quit_app(self):
        self.tray_icon.stop()
        QApplication.quit()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WallpaperApp()
    ex.show()
    sys.exit(app.exec_())
