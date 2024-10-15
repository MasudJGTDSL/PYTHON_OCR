import qrcode
import re
from datetime import datetime
result_files = "QRcode_output/"

date_now = datetime.now().strftime("%Y%m%d%H%M")

class Qrcode_generator():
    def __init__(self, text):
        self.text = text
        self.generate_qrcode()
    
    def generate_qrcode(self):
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants. ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"{result_files}QRCODE_{date_now}.png")


txt = """Md. Masud Zaman\n
Nurani-12/2B, Boncolapara,\n
Subidbazar, Sylhet-3100\n
Mobile: +8801712623231\n
website: https://mahimsoft.com.bd/
"""


if __name__ == '__main__': 
    oc = Qrcode_generator(text=txt) 


#!TO RUN: python QRCODE_generator.py