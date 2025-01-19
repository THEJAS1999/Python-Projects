import os
import qrcode
from datetime import datetime

# URL to be encoded in the QR code
URL = "https://www.google.com/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(URL)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')
name = f"qrcode{datetime.now().strftime("%d%b%y%H%M%S")}.png"

# Save the image to a file in the same directory as the Python file
file_path = os.path.join(os.path.dirname(__file__), name)
img.save(file_path)