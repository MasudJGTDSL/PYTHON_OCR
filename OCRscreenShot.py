import sys
import os
import time
import subprocess
import pyperclip
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QFileDialog, QPlainTextEdit, QStyle
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QFont, QFontDatabase
from PIL import ImageGrab
import pyautogui

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'ScreenGrab-OCR --মাহিম সফ্‌ট'
        self.width = 640
        self.height = 640
        self.left = int((pyautogui.size()[0]-self.width)/2)
        self.top = int((pyautogui.size()[1]-self.height)/2)
        self.setWindowIcon(self.style().standardIcon(getattr(QStyle, 'SP_DesktopIcon')))
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("Click the button below to capture or load a screenshot.")
        self.grid.addWidget(self.label, 0, 0)
        
        self.button = QPushButton('Capture Screenshot (Whole Screen)', self)
        self.button.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DesktopIcon')))
        self.button.setToolTip('Click to capture a screenshot of your entire screen. (Not recommended)')
        self.button.clicked.connect(self.on_click_capture)
        self.grid.addWidget(self.button, 1, 0)

        self.button = QPushButton('Upload Screenshot', self)
        self.button.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DialogOpenButton')))
        self.button.setToolTip('Click to upload it from the local storage.')
        self.button.clicked.connect(self.on_click_upload)
        self.grid.addWidget(self.button, 2, 0)

        self.button = QPushButton('Load Screenshot from Clipboard', self)
        self.button.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_FileDialogContentsView')))
        self.button.setToolTip('Click to upload it from your clipboard.')
        self.button.clicked.connect(self.on_click_clipboard)
        self.grid.addWidget(self.button, 3, 0)
        
        self.textbox = QPlainTextEdit(self)
        self.textbox.setReadOnly(False)
        self.textbox.setFont(QFont('Shonar Bangla', 11))
        self.textbox.setPlainText("Ready to capture a screenshot.\nRequires installation of Tesseract Open Source OCR Engine.\nLink: https://tesseract-ocr.github.io/tessdoc/Installation.html\n--মাহিম সফ্ট, ঢাকা, বাংলাদেশ।")
        self.grid.addWidget(self.textbox, 4, 0)
        
        self.show()

    @pyqtSlot()
    def on_click_capture(self):
        self.label.setText("Processing...")
        self.button.setEnabled(False)
        self.textbox.setPlainText("")
        self.update()
        time.sleep(0.1)
        t_start = time.perf_counter()
        self.capture_screenshot()
        self.perform_ocr()
        self.button.setEnabled(True)
        self.label.setText("The OCR result has been copied to your clipboard.\nLast run: {:.2f} seconds".format(time.perf_counter() - t_start))
        self.update()

    def on_click_upload(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self,"Upload the screenshot from local storage.", "","All Files (*);;PNG Files (*.png)", options=options)
        if filename:
            self._extracted_from_on_click_upload_6(filename)

    # TODO Rename this here and in `on_click_upload`
    def _extracted_from_on_click_upload_6(self, filename):
        self.label.setText("Processing...")
        self.button.setEnabled(False)
        self.textbox.setPlainText("")
        self.update()
        time.sleep(0.1)
        t_start = time.perf_counter()
        self.perform_ocr(filename)
        self.button.setEnabled(True)
        self.label.setText("The OCR result has been copied to your clipboard.\nLast run: {:.2f} seconds".format(time.perf_counter() - t_start))
        self.update()

    def on_click_clipboard(self):
        self.label.setText("Processing...")
        self.button.setEnabled(False)
        self.textbox.setPlainText("")
        self.update()
        time.sleep(0.1)
        t_start = time.perf_counter()
        try:
            self._extracted_from_on_click_clipboard_9(t_start)
        except Exception:
            self.label.setText("Click the button below to capture or load a screenshot.")
            self.textbox.setPlainText("No image found in the clipboard.")
            self.button.setEnabled(True)
            self.update()
            return

    # TODO Rename this here and in `on_click_clipboard`
    def _extracted_from_on_click_clipboard_9(self, t_start):
        imgrab = ImageGrab.grabclipboard()
        imgrab.save('screenshot.png','PNG')
        self.perform_ocr()
        self.button.setEnabled(True)
        self.label.setText("The OCR result has been copied to your clipboard.\nLast run: {:.2f} seconds".format(time.perf_counter() - t_start))
        self.update()

    def capture_screenshot(self):
        width, height= pyautogui.size()
        monitor_screen = (0, 0, width, height)
        scrgrab = pyautogui.screenshot(region=(monitor_screen))
        scrgrab.save(r'screenshot.png')

    def perform_ocr(self, filename="screenshot.png"):
        try:
            subprocess.run(["tesseract", filename, "screenshot", "-l", "ben+eng"])
        except FileNotFoundError:
            self.textbox.setPlainText("Tesseract is not installed. Please install it first.")
            return
        except Exception as e:
            self.textbox.setPlainText(
                f"An error occurred while performing OCR.\nError: {e}"
            )
            return
        with open("screenshot.txt", "r") as f:
            text = f.read()
        pyperclip.copy(text)
        self.textbox.setPlainText(text)
        # Delete 'screenshot.png' and 'screenshot.txt' files if it exists in the current directory
        if os.path.exists("screenshot.png"):
            os.remove("screenshot.png")
        if os.path.exists("screenshot.txt"):
            os.remove("screenshot.txt")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())



# python screenShot.py