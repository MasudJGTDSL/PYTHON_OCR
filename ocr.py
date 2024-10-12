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
#? To Run: python ocr.py
"""

from PIL import Image 
import pytesseract as pt 
import os 

tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def main(): 
    # path for the folder for getting the raw images 
    path =r".\Images"

    # path for the folder for getting the output 
    tempPath =r".\Text Files"

    # iterating the images inside the folder 
    for imageName in os.listdir(path): 

        inputPath = os.path.join(path, imageName) 
        img = Image.open(inputPath) 

        # applying ocr using pytesseract for python 
        text = pt.image_to_string(img, lang ="ben") 

        # for removing the .jpg from the imagePath 
        # imagePath = imagePath[0:-4] 

        fullTempPath = os.path.join(tempPath, imageName[0:-4]+".txt") 
        # print(text) 

        # saving the  text for every image in a separate .txt file 
        file1 = open(fullTempPath, "w") 
        file1.write(text) 
        file1.close()  

if __name__ == '__main__': 
    main() 