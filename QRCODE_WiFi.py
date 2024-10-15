from datetime import datetime
import wifi_qrcode_generator.generator


date_now = datetime.now().strftime("%Y%m%d%H%M")
def generate_wifi_qrcode(ssid,auth_type,pw):
    qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
        ssid=ssid, hidden=False, authentication_type=auth_type, password=pw
    )
    qr_code.print_ascii()
    qr_code.make_image().save(fr'./QRcode_output/WiFi_{date_now}.png')

if __name__ == '__main__': 
    generate_wifi_qrcode('your_ssid','WPA','wifi_password') 


#!TO Run: python QRCODE_WiFi.py
