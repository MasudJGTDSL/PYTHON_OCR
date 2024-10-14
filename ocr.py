"""
#!Install Tesseract on Windows:
On Windows, download the installer from the official Tesseract GitHub repository and run it.
#* https://github.com/UB-Mannheim/tesseract/wiki

#!Add Tesseract to your PATH:
On Windows:
Search for 'Environment Variables' in the start menu and select 'Edit the system environment variables'.
Click on the 'Environment Variables' button.
Under 'System Variables', find the 'Path' variable and click 'Edit'.
Add the path to the Tesseract executable (e.g., C:\Program Files\Tesseract-OCR) to the list.
Click 'OK' to save the changes.

#! Point pytesseract to where the Tesseract executable is located
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  
#* Update the path as needed
#! To Run: python ocr.py
"""

from PIL import Image 
import pytesseract as pt 
import os 

tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# path for the folder for getting the raw images 
path = r".\Images"
# path for the folder for getting the output 
textPath = r".\Text_Files"

class Ocr():
    def __init__(self, path, text_files):
        self.path = path
        self.text_files = text_files
        self.main()
    def main(self): 
        # iterating the images inside the folder
        for imageName in os.listdir(self.path): 
            inputPath = os.path.join(self.path, imageName)
            img = Image.open(inputPath) 
            # applying ocr using pytesseract for python 
            text = pt.image_to_string(img, lang ="ben") 
            fullTempPath = os.path.join(self.text_files, f"{imageName[:-4]}.txt")
            with open(fullTempPath, "w") as file1:
                file1.write(text)  

if __name__ == '__main__': 
    oc = Ocr(path=path, text_files=textPath) 