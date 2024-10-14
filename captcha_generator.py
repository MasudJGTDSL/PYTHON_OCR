import random
import string
from io import BytesIO
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha

def generate_random_captcha(length=6):
    return ''.join(random.choice(string.digits) for _ in range(length))

def generate_random_captcha_text(length=6):
    return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(length))

audio = AudioCaptcha()
captcha_numbers = generate_random_captcha()
audio_captcha = audio.generate(captcha_numbers)
audio.write(captcha_numbers, './captcha_/Audio_Captcha.wav')
#cLcoding.com

captcha_text = generate_random_captcha_text()
audio = AudioCaptcha()
image = ImageCaptcha(fonts=['./captcha_/LCALLIG.TTF', './captcha_/CHILLER.TTF'])
data = audio.generate(captcha_numbers)
audio.write(captcha_numbers, './captcha_/captcha.wav')
data = image.generate(captcha_text)
print(captcha_numbers)
print(captcha_text)
image.write(captcha_text, './captcha_/captcha.png')