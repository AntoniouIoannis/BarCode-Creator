import pyqrcode
from PIL import Image
import time
link = input('Εισαγάγετε οτιδήποτε για να δημιουργήσετε το QR: ')
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=6)
Image.open("QRCode.png")
print('processing...')
time.sleep (5)
print('Το barcode δημιουργήθηκε\nΑναζητήστε την φωτο QRCode.png στον κατάλογο σας.')
