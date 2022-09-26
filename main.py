import pyqrcode
from PIL import Image
import time
link = input('Enter anything to qenerate QR: ')
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=6)
Image.open("QRCode.png")
print('processing...')
time.sleep (5)
print('BarCode completed.')
