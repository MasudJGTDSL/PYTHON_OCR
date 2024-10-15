from datetime import datetime
from PIL import Image, ImageDraw, ImageOps
from typing import Optional
import qrcode

salu = "Md."
last_name = "Zaman"
first_name = "Masud"
full_name = f"{salu} {first_name} {last_name}"
date_of_birth = r"20000101"
organization = "Mahim Soft"
job_title = "Proprietor"
photo = "https://lh3.googleusercontent.com/contacts/AG6tpzFmasVgWdFZ3psk8vFe5xaVFYh8-z0A3sXE4Zh3LCt8AhSAHKRU=s408-p-k-rw-no"

address_work_1 = r"AeroSky Tower"
address_work_2 = r"Bawnia, Turag"
address_work_3 = r"Dhaka"
address_work_4 = r"1231"
address_work_5 = r"Bangladesh"
address_work = f"{address_work_1}\n{address_work_2}\n{address_work_3}-{address_work_4}\n{address_work_5}"

address_home_1 = r"Nurani-12/2B"
address_home_2 = r"Bonkolapara, Subidbazar"
address_home_3 = r"Sylhet"
address_home_4 = r"3100"
address_home_5 = r"Bangladesh"
address_home = f"{address_home_1}\n{address_home_2}\n{address_home_3}-{address_home_4}\n{address_home_5}"
mobile_home = r"+8801712623231"
mobile_work = r"+8801778010166"
email_personal = r"masud.jgtdsl@gmail.com"
email_work = r"mahim.softs@gmail.com"
website = r"https://www.mahimsoft.com"

date_now = datetime.now() #.strftime("%Y%m%d%H%M")

# VCARD = f"""
# BEGIN:VCARD
# VERSION:3.0
# N:{last_name};{first_name};;{salu};
# FN:{full_name}
# ORG:{organization}
# TITLE:{job_title}
# PHOTO;VALUE#URI;TYPE#GIF:{photo}
# TEL;TYPE#WORK,VOICE:{mobile_work}
# TEL;TYPE#HOME,VOICE:{mobile_home}
# ADR;TYPE#WORK,PREF:;;{address_work_1};{address_work_2};{address_work_1};{address_work_4};{address_work_5}
# LABEL;TYPE#WORK,PREF:{address_work}
# ADR;TYPE#HOME:;;{address_home_1};{address_home_2};{address_home_3};{address_home_4};{address_home_5}
# LABEL;TYPE#HOME:{address_home}
# EMAIL:{email_personal}
# REV:{date_now}
# END:VCARD
# """

# VCARD = f"""BEGIN:VCARD
# VERSION:3.0
# N:Lastname;Surname
# FN:Displayname
# ORG:EVenX
# URL:http://www.evenx.com/
# EMAIL:info@evenx.com
# TEL;TYPE=voice,work,pref:+49 1234 56788
# ADR;TYPE=intl,work,postal,parcel:;;Wallstr. 1;Berlin;;12345;Germany
# END:VCARD"""

VCARD = f"""BEGIN:VCARD
VERSION:3.0
N:{last_name};{first_name};;{salu};
FN:{full_name}
BDAY:{date_of_birth}
ADR;type=HOME:;;{address_home_1};{address_home_2};{address_home_3};{address_home_4};{address_home_5}
TEL;type=CELL:{mobile_home}
TZ:Asia/Dhaka
EMAIL;type=PERSONAL,INTERNET:{email_personal}
ORG:{organization};
TITLE:{job_title}
EMAIL;type=WORK,INTERNET:{email_work}
URL:{website}
REV:{datetime.now()}
END:VCARD"""


def generate_masked_inner_img(inner_img_path: str):
    """Create an inner image with a circular mask for center of QR code."""
    img = Image.open(inner_img_path).convert("RGBA")
    img_width, img_height = img.size

    # Create a circular mask for the inner image
    mask = Image.new("L", (img_width, img_height), 0)
    draw = ImageDraw.Draw(mask)
    circle_center = (img_width // 2, img_height // 2)
    circle_radius = min(img_width, img_height) // 2
    draw.ellipse(
        (
            circle_center[0] - circle_radius,
            circle_center[1] - circle_radius,
            circle_center[0] + circle_radius,
            circle_center[1] + circle_radius,
        ),
        fill=255,
    )

    # Apply the circular mask to the inner image
    img = Image.composite(
        img,
        Image.new("RGBA", img.size, (255, 255, 255, 255)),
        mask
    )

    padding = 20  # Adjust the padding as needed

    # Use ImageOps.expand to create a canvas with a white background and padding
    return ImageOps.expand(img, border=padding, fill="white")


def create_qr_code(output_path: str, inner_img_path: str):
    """Create QR code image from content to output path with a inner imgage"""
    qr_object = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr_object.add_data(VCARD)
    qr_object.make(fit=True)

    img = qr_object.make_image(fill_color="black", back_color="white").convert("RGBA")

    inner_img = generate_masked_inner_img(inner_img_path)

    # Paste the canvas onto the QR code image
    img.paste(
        inner_img,
        (
            img.width // 2 - inner_img.width // 2,
            img.height // 2 - inner_img.height // 2
        ),
        mask=inner_img.split()[3],
    )

    img.save(output_path)

out_path = fr"./TMP/{full_name}_{date_now.strftime('%Y%m%d%H%M')}.png"
in_path = r"./TMP/MS3.png"

if __name__ == "__main__":
    create_qr_code(out_path,in_path)

#! TO Run: python QRCODE_vcard.py